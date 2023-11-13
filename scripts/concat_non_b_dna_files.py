import argparse
import glob
from os import path

import pandas as pd


def concat_nBMST_output_files(input_dir, output_file, chromosome_name, non_b_dna_type,
                              input_file_extension, non_b_dna_skip_list):
  if non_b_dna_type is None:
    file_names = glob.glob(path.join(input_dir, chromosome_name + "_*" + input_file_extension))
  else:
    file_names = glob.glob(path.join(input_dir, chromosome_name + "_" + non_b_dna_type + input_file_extension))

  df_all = pd.DataFrame()

  for file_name in file_names:
    print(f"file_name: {file_name}")
    if not non_b_dna_skip_list is None:
      for non_b_dna_skip_type in non_b_dna_skip_list:
        if non_b_dna_skip_type in file_name:
          print(f"Skipping {file_name} as it is in non-b DNA skip list: {non_b_dna_skip_list}")
          continue

    if input_file_extension == ".tsv":
      df = pd.read_csv(file_name, sep='\t')[["Start", "Stop", "Strand"]]
      df.rename(columns={"Start": "chromStart", "Stop": "chromEnd", "Strand": "strand"}, inplace=True)
      df.insert(0, "chrom", chromosome_name)
    elif input_file_extension == ".bed":
      df = pd.read_csv(file_name, sep='\t', names=["chrom", "chromStart", "chromEnd", "strand"])
    df.chromStart = df.chromStart.astype(int)
    df.chromEnd = df.chromEnd.astype(int)
    print(df.head(1))
    df_all = pd.concat([df_all, df], axis=0)

  print(f'df_all.shape[0]: {df_all.shape[0]}')
  print(df_all.head(1))
  df_all.sort_values(by=['chromStart', 'chromEnd'], inplace=True)
  df_all.to_csv(output_file, index=False, sep="\t", header=False)


if __name__ == "__main__":
  argParser = argparse.ArgumentParser("Concatenate nBMST output files")
  argParser.add_argument("-i", "--input_dir", type=str, required=True)
  argParser.add_argument("-o", "--output_file", type=str, required=True)
  argParser.add_argument("-c", "--chromosome_name", type=str, required=True)
  argParser.add_argument("-n", "--non_b_dna_type", type=str, choices=["GQ", "MR", "STR", "APR", "IR", "DR", "Z"])
  argParser.add_argument("-e", "--input_file_extension", type=str, default=".tsv")
  argParser.add_argument("-s", "--non_b_dna_skip_list", nargs="+", help="Skip these non-B DNA types when aggregating all")
  args = argParser.parse_args()
  concat_nBMST_output_files(args.input_dir, args.output_file, args.chromosome_name, args.non_b_dna_type,
                            args.input_file_extension, args.non_b_dna_skip_list)

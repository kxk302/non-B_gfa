import argparse
import glob
from os import path

import pandas as pd


def concat_nBMST_output_files(input_dir, output_file, chromosome_name, non_b_dna_type):
  if non_b_dna_type is None:
    file_names = glob.glob(path.join(input_dir, chromosome_name + "*.tsv"))
  else:
    file_names = glob.glob(path.join(input_dir, chromosome_name + "_" + non_b_dna_type + ".tsv"))

  df_all = pd.DataFrame()

  for file_name in file_names:
    print(f"file_name: {file_name}")
    df = pd.read_csv(file_name, sep='\t')[["Start", "Stop", "Strand"]]
    df.rename(columns={"Start": "chromStart", "Stop": "chromEnd", "Strand": "strand"}, inplace=True)
    df.insert(0, "chrom", chromosome_name)
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
  argParser.add_argument("-c", "--chromosome_name", type=str, required=True, choices=["chrX", "chrY"])
  argParser.add_argument("-n", "--non_b_dna_type", type=str, choices=["GQ", "MR", "STR", "APR", "IR", "DR", "Z"])
  args = argParser.parse_args()
  concat_nBMST_output_files(args.input_dir, args.output_file, args.chromosome_name, args.non_b_dna_type)

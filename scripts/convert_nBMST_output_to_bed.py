import argparse
from os import path
from pathlib import Path

import pandas as pd


def convert_nBMST_output_to_bed(input_file, output_folder):
  if path.getsize(input_file) == 0:
    print(f"File {input_file} has size of 0")
    return
  df = pd.read_csv(input_file, sep='\t')[["Sequence_name", "Start", "Stop", "Strand"]]
  df.rename(columns={"Start": "chromStart", "Stop": "chromEnd", "Strand": "strand"}, inplace=True)
  df["chrom"] = df["Sequence_name"].str.split(':').str[0]
  df.drop(columns=["Sequence_name"], inplace=True)
  df.chromStart = df.chromStart.astype(int)
  df.chromEnd = df.chromEnd.astype(int)
  df=df[["chrom", "chromStart", "chromEnd", "strand"]]
  file_name = Path(input_file).stem
  output_file = path.join(output_folder, file_name + ".bed")
  df.sort_values(by=['chromStart', 'chromEnd'], inplace=True)
  df.to_csv(output_file, index=False, sep="\t", header=False)


if __name__ == "__main__":
  argParser = argparse.ArgumentParser("Concatenate nBMST output files")
  argParser.add_argument("-i", "--input_file", type=str, required=True)
  argParser.add_argument("-o", "--output_folder", type=str, required=True)
  args = argParser.parse_args()
  convert_nBMST_output_to_bed(args.input_file, args.output_folder)

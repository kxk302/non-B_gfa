import argparse
import glob
import os

import pandas as pd


def standardize_chromosome_name(input_folder):
  bed_files = glob.glob(input_folder+ "/*merged.bed")
  for bed_file in bed_files:
    print(f"bed_file: {bed_file}")
    bed_file_name = os.path.basename(bed_file)
    undescore_index = bed_file_name.index("_")
    chromosome_name = bed_file_name[0: undescore_index]
    print(f"chromosome_name: {chromosome_name}")

    df = pd.read_csv(bed_file, sep="\s+", names=["chr", "start", "end"])
    print(f"df.shape: {df.shape}")

    # If bed file is not empty
    if df.shape[0] > 0:
      print(df.head(2))
      df["chr"] = chromosome_name
      print(df.head(2))
      df.to_csv(bed_file, sep="\t", index=False, header=False)


if __name__ == "__main__":
  argParse = argparse.ArgumentParser("Standardize chromosome name in first column of bed file")
  argParse.add_argument("-i", "--input_folder", type=str, required=True)
  args = argParse.parse_args()
  standardize_chromosome_name(args.input_folder)


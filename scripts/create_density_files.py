import argparse

import pandas as pd


def create_density_file(input_file, output_file, chromosome_name):
  df = pd.read_csv(input_file, sep='\t', names=["chr", "start", "stop", "index", "count"])
  df = df.drop(["chr", "index"], axis=1)
  df = df.astype({"count": bool})
  density = df.groupby(by=["start", "stop"]).sum()
  density.reset_index(inplace=True)
  density.insert(0, "chr", chromosome_name)
  print(density.head(5))
  density.to_csv(output_file, index=False, sep="\t")


if __name__ == "__main__":
  argParser = argparse.ArgumentParser("Create density file")
  argParser.add_argument("-i", "--input_file", type=str, required=True)
  argParser.add_argument("-o", "--output_file", type=str, required=True)
  argParser.add_argument("-c", "--chromosome_name", type=str, required=True, choices=["chrX", "chrY"])
  args = argParser.parse_args()
  create_density_file(args.input_file, args.output_file, args.chromosome_name)

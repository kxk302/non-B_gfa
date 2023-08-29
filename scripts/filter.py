import argparse
from os import path

import pandas as pd
import Bio.SeqIO as IO

def filter(nBMST_output_file, spacer_length_filter, output_file):
  df = pd.read_csv(nBMST_output_file, sep="\t")

  print(f'spacer length filter is {spacer_length_filter}')
  print(f'df.shape prior to filtering: {df.shape}')
  df = df[df.Spacer <= spacer_length_filter]
  print(f'df.shape after filtering: {df.shape}')

  df.to_csv(output_file, index=False, sep="\t")


if __name__ == "__main__":
  argParser = argparse.ArgumentParser("This script filters an nBMST output .tsv file based on spacer length")

  argParser.add_argument("-n", "--nBMST_output_file", type=str, required=True)
  argParser.add_argument("-f", "--spacer_length_filter", type=int, required=True)
  argParser.add_argument("-o", "--output_file", type=str, required=True)
  args = argParser.parse_args()

  filter(args.nBMST_output_file, args.spacer_length_filter, args.output_file)

import argparse
from os import path 

import pandas as pd
  
chromosomes = ["chrX", "chrY"]
non_b_dna_types = ["APR", "DR", "GQ", "IR", "MR", "STR", "Z"]
non_b_dna_dict = {
    "APR": "A-Phased Repeats",
    "DR": "Direct Repeats",
    "GQ": "G-Quadruplex",
    "IR": "Inverted Repeats",
    "MR": "Mirror Repeats",
    "STR": "Short Tandem Repeats",
    "Z": "Z DNA",
  }
repeat_types = [
  "Satellite",
  "Satellite_acro",
  "Satellite_centr",
  "Satellite_subtelo",
  "Satellite_Y-chromosome",
  "Simple_repeat",
]

#  "Unspecified_SAT",
#  "Unspecified_StSat_pCHT",

def summarize_repeats(species, repeats_folder, output_file):
  zero_list = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
  data = {
    "APR": zero_list,
    "DR": zero_list,
    "GQ": zero_list,
    "IR": zero_list,
    "MR": zero_list,
    "STR": zero_list,
    "Z": zero_list,
  }

  repeats_length_sum = pd.Series(data=zero_list, index=repeat_types)
  intersect_length_sum = pd.DataFrame(data=data, index=repeat_types)

  # Populate repeat length Series. Add chrX and chrY values to the same cell.
  # We'd end up with len(repeat_types) values
  for chromosome in chromosomes:
    for repeat_type in repeat_types:
      file_path = path.join(repeats_folder, species, chromosome + "_" + repeat_type + "_merged.bed")
      try:
        df = pd.read_csv(file_path, sep="\t", names=["chr", "start", "stop"])
      except pd.errors.EmptyDataError:
        print("The TSV file is empty. No need to update repeats length series")
      else:
        df["length"] = df["stop"] - df["start"] + 1
        repeats_length_sum[repeat_type] += df["length"].sum()

  # print(repeats_length_sum)

  # Populate intersect length DataFrame. Add chrX and chrY values to the same cell.
  # We'd end up with len(repeat_types) X len(non_b_dna_types) values
  for chromosome in chromosomes:
    for repeat_type in repeat_types:
      for non_b_dna_type in non_b_dna_types:
        file_path = path.join(repeats_folder, species, chromosome + "_" + repeat_type + "_intersect_" + non_b_dna_type + ".bed")
        try:
          df = pd.read_csv(file_path, sep="\t", names=["chr", "start", "stop"])
        except pd.errors.EmptyDataError:
          print("The CSV file is empty")
          print("The TSV file is empty. No need to update intersect length dataframe")
        else:
          df["length"] = df["stop"] - df["start"] + 1
          intersect_length_sum.loc[repeat_type, non_b_dna_type] += df["length"].sum()

  # print(intersect_length_sum)

  # Divide intersect length table rows by corresponding repeat length table values
  # This results in cell values beingbetween 0 and 1
  for repeat_type in repeat_types:
    if repeats_length_sum[repeat_type] != 0.00:
      intersect_length_sum.loc[repeat_type] /= repeats_length_sum[repeat_type]

  # print(intersect_length_sum)
  intersect_length_sum.to_csv(output_file, sep="\t")


if __name__ == "__main__":
  argParser = argparse.ArgumentParser("This script summarizes nBMST results")

  argParser.add_argument("-s", "--species", type=str, required=True,
                         choices=["Bonobo", "Chimpanzee", "Human", "Gorilla", "B_Orangutan", "S_Orangutan", "Siamang"])
  argParser.add_argument("-f", "--repeats_folder", type=str, required=True)
  argParser.add_argument("-o", "--output_file", type=str, required=True)
  
  args = argParser.parse_args()
  
  summarize_repeats(args.species, args.repeats_folder, args.output_file)

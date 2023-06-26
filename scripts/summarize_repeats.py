import argparse
import os
from os import path 

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
  
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
  "DNA",
  "DNA/Crypton",
  "DNA/Crypton-A",
  "DNA/Kolobok",
  "DNA/MULE-MuDR",
  "DNA/Merlin",
  "DNA/PIF-Harbinger",
  "DNA/PiggyBac",
  "DNA/TcMar",
  "DNA/TcMar-Mariner",
  "DNA/TcMar-Pogo",
  "DNA/TcMar-Tc1",
  "DNA/TcMar-Tc2",
  "DNA/TcMar-Tigger",
  "DNA/hAT",
  "DNA/hAT-Ac",
  "DNA/hAT-Blackjack",
  "DNA/hAT-Charlie",
  "DNA/hAT-Tag1",
  "DNA/hAT-Tip100",
  "DNA/hAT-Tip100?",
  "DNA/hAT-hAT19",
  "DNA/hAT?",
  "DNA?/hAT-Tip100?",
  "LINE/CR1",
  "LINE/Dong-R4",
  "LINE/I-Jockey",
  "LINE/L1",
  "LINE/L1-Tx1",
  "LINE/L2",
  "LINE/Penelope",
  "LINE/RTE-BovB",
  "LINE/RTE-X",
  "LTR",
  "LTR/ERV1",
  "LTR/ERVK",
  "LTR/ERVL",
  "LTR/ERVL-MaLR",
  "LTR/Gypsy",
  "Low_complexity",
  "RC/Helitron",
  "Retroposon/SVA",
  "SINE/5S-Deu-L2",
  "SINE/Alu",
  "SINE/MIR",
  "SINE/tRNA",
  "SINE/tRNA-Deu",
  "SINE/tRNA-RTE",
  "Satellite",
  "Satellite/Y-chromosome",
  "Satellite/acro",
  "Satellite/centr",
  "Satellite/subtelo",
  "Simple_repeat",
  "Unknown",
  "Unspecified",
  "rRNA",
  "scRNA",
  "snRNA",
  "srpRNA",
  "tRNA",
]

species_to_folder_dict = {
  "B_Orangutan": "Bornean",
  "Bonobo": "Bonobo",
  "Chimpanzee": "Chimpanzee",
  "Gorilla": "Gorilla",
  "Human": "CHM13v2.0_XY",
  "S_Orangutan": "Sumatran",
  "Siamang": "Siamang",
}

REPEATS_FILE_COLUMNS = [4, 5, 6, 9, 10]
REPEATS_COLUMN_NAMES = ["chromosome", "start", "stop", "sub_label", "label"]

def summarize_repeats(species, repeats_folder, nbmst_output_folder, output_file):
  zero_list = [0.00] * len(repeat_types)
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
      file_path = path.join(repeats_folder, species, chromosome + "_" + repeat_type.replace("/", "_") + "_merged.bed")
      try:
        df = pd.read_csv(file_path, sep="\t", names=["chr", "start", "stop"])
      except pd.errors.EmptyDataError:
        print("The TSV file is empty. No need to update repeats length series")
      else:
        df["length"] = df["stop"] - df["start"] + 1
        repeats_length_sum[repeat_type] += df["length"].sum()

  # Populate intersect length DataFrame. Add chrX and chrY values to the same cell.
  # We'd end up with len(repeat_types) X len(non_b_dna_types) values
  for chromosome in chromosomes:
    for repeat_type in repeat_types:
      for non_b_dna_type in non_b_dna_types:
        file_path = path.join(repeats_folder, species, chromosome + "_" + repeat_type.replace("/", "_") + "_intersect_" + non_b_dna_type + ".bed")
        try:
          df = pd.read_csv(file_path, sep="\t", names=["chr", "start", "stop"])
        except pd.errors.EmptyDataError:
          print("The CSV file is empty")
          print("The TSV file is empty. No need to update intersect length dataframe")
        else:
          df["length"] = df["stop"] - df["start"] + 1
          intersect_length_sum.loc[repeat_type, non_b_dna_type] += df["length"].sum()


  # Divide intersect length table rows by corresponding repeat length table values
  # This results in cell values beingbetween 0 and 1
  for repeat_type in repeat_types:
    if repeats_length_sum[repeat_type] != 0.00:
      intersect_length_sum.loc[repeat_type] /= repeats_length_sum[repeat_type]

  # Add column with the number of repeat elements in each category, per species
  repeats_file = path.join(repeats_folder, "input", species_to_folder_dict[species] + "_FinalAnnotations_June2023_v2.sort.out")
  repeats_df = pd.read_csv(repeats_file, sep="\t", usecols=REPEATS_FILE_COLUMNS, names=REPEATS_COLUMN_NAMES)
  number_of_repeat_types = repeats_df['label'].value_counts().sort_index()

  # Add new column
  intersect_length_sum["number_of_repeat_types"] = number_of_repeat_types

  # Add row with average non-B density per non-B type, per species
  average_non_b_dna_density = get_average_non_b_dna_density(nbmst_output_folder)
  average_non_b_dna_density_list = average_non_b_dna_density.tolist()
  average_non_b_dna_density_list.append(0.00)
  print(f'average_non_b_dna_density_list: {average_non_b_dna_density_list}')
  intersect_length_sum.loc["avg_non_b_dna_density"] = average_non_b_dna_density_list

  intersect_length_sum.to_csv(output_file, sep="\t")


def get_average_non_b_dna_density(nbmst_output_folder):
  zero_list = [0.00] * len(non_b_dna_types)
  average_non_b_dna_density = pd.Series(data=zero_list, index=non_b_dna_types)

  # Read chrX and chrY lengths and add them to get total length
  chrX_file_path = path.join(nbmst_output_folder, "chrX.txt")
  chrY_file_path = path.join(nbmst_output_folder, "chrY.txt")

  df_chr_x = pd.read_csv(chrX_file_path, sep="\t", names=["chr","length"])
  df_chr_y = pd.read_csv(chrY_file_path, sep="\t", names=["chr","length"])

  total_length = (df_chr_x["length"] + df_chr_y["length"])[0]

  # For each non-B DNA type, and for chrX and chrY, add the
  # non-B DNA total length to the series
  for non_b in non_b_dna_types:
    for chr in chromosomes:
      file_path = path.join(nbmst_output_folder, chr + "_" + non_b + ".bed")
      non_b_df = pd.read_csv(file_path, sep="\t", names=["chr", "start", "stop", "strand"])
      non_b_df["length"] = non_b_df["stop"] - non_b_df["start"]  + 1
      average_non_b_dna_density[non_b] += non_b_df["length"].sum()

  # Divide non-B DNA total length (for both chrX and chrY) by total length
  # (for both chrX and chrY), so non-B DNA total length is normalized
  print(f'total_length: {total_length}')
  print(f'average_non_b_dna_density: {average_non_b_dna_density}')
  print(f'average_non_b_dna_density.div(total_length): {average_non_b_dna_density.div(total_length)}')
  return average_non_b_dna_density.div(total_length)


if __name__ == "__main__":
  argParser = argparse.ArgumentParser("This script summarizes nBMST results")

  argParser.add_argument("-s", "--species", type=str, required=True,
                         choices=["Bonobo", "Chimpanzee", "Human", "Gorilla", "B_Orangutan", "S_Orangutan", "Siamang"])
  argParser.add_argument("-f", "--repeats_folder", type=str, required=True)
  argParser.add_argument("-n", "--nbmst_output_folder", type=str, required=True)
  argParser.add_argument("-o", "--output_file", type=str, required=True)
  
  args = argParser.parse_args()
  
  summarize_repeats(args.species, args.repeats_folder, args.nbmst_output_folder, args.output_file)

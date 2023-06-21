import argparse
from os import path

import pandas as pd

REPEATS_FILE_COLUMNS = [4, 5, 6, 9, 10]
REPEATS_COLUMN_NAMES = ["chromosome", "start", "stop", "sub_label", "label"]
REPEAT_LABELS = [
  "Satellite", 
  "Satellite/acro", 
  "Satellite/centr", 
  "Satellite/subtelo", 
  "Satellite/Y-chromosome", 
  "Simple_repeat",
  "Unspecified",
  "Unspecified"
]
REPEAT_SUBLABELS = [
  "", 
  "", 
  "", 
  "", 
  "", 
  "",
  "SAT",
  "StSat_pCHT"
  ]
CHROMOSOMES = ["chrX", "chrY"]

def create_repeat_files(species, repeats_file, output_folder):
  repeats_df = pd.read_csv(repeats_file, sep="\t", usecols=REPEATS_FILE_COLUMNS, names=REPEATS_COLUMN_NAMES)

  for index, label in enumerate(REPEAT_LABELS):
    for chromosome in CHROMOSOMES:
      sub_label = REPEAT_SUBLABELS[index]
      print(f"label: <{label}>, sub_label: <{sub_label}>")
      
      if sub_label == "":
        df_label = repeats_df[ (repeats_df.label == label) & 
                               (repeats_df.chromosome == chromosome) ]
        #print(df_label.head())
        output_file_path = path.join(output_folder, species, chromosome + "_" + label.replace("/", "_") + ".bed")
      else:
        df_label = repeats_df[ (repeats_df.label == label) & 
                               (repeats_df.sub_label.str.startswith(sub_label)) &
                               (repeats_df.chromosome == chromosome) ]
        #print(df_label.head())
        output_file_path = path.join(output_folder, species, chromosome + "_" + label.replace("/", "_") + "_" + sub_label + ".bed")

      df_label.to_csv(output_file_path, columns=["chromosome", "start", "stop"], header=False, index=False, sep="\t")


if __name__ == "__main__":

  argumentParser = argparse.ArgumentParser("Create merged (no overlap) repeat files for a species, for each repeat/satellite type")

  argumentParser.add_argument("-s", "--species", type=str, required=True, 
                              choices=["Bonobo", "Chimpanzee", "Human", "Gorilla", "B_Orangutan", "S_Orangutan", "Siamang"])
  argumentParser.add_argument("-f", "--repeats_file", type=str, required=True)
  argumentParser.add_argument("-o", "--output_folder", type=str, required=True) 

  args = argumentParser.parse_args()

  create_repeat_files(args.species, args.repeats_file, args.output_folder)

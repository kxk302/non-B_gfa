import argparse
from os import path

import pandas as pd

REPEATS_FILE_COLUMNS = [4, 5, 6, 9, 10]
REPEATS_COLUMN_NAMES = ["chromosome", "start", "stop", "sub_label", "label"]
REPEAT_LABELS = [
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
CHROMOSOMES = ["chrX", "chrY"]

def create_repeat_files(species, repeats_file, output_folder):
  repeats_df = pd.read_csv(repeats_file, sep="\t", usecols=REPEATS_FILE_COLUMNS, names=REPEATS_COLUMN_NAMES)

  for index, label in enumerate(REPEAT_LABELS):
    for chromosome in CHROMOSOMES:
      df_label = repeats_df[ (repeats_df.label == label) &
                             (repeats_df.chromosome == chromosome) ]
      output_file_path = path.join(output_folder, species, chromosome + "_" + label.replace("/", "_") + ".bed")

      df_label.to_csv(output_file_path, columns=["chromosome", "start", "stop"], header=False, index=False, sep="\t")


if __name__ == "__main__":

  argumentParser = argparse.ArgumentParser("Create merged (no overlap) repeat files for a species, for each repeat/satellite type")

  argumentParser.add_argument("-s", "--species", type=str, required=True, 
                              choices=["Bonobo", "Chimpanzee", "Human", "Gorilla", "B_Orangutan", "S_Orangutan", "Siamang"])
  argumentParser.add_argument("-f", "--repeats_file", type=str, required=True)
  argumentParser.add_argument("-o", "--output_folder", type=str, required=True) 

  args = argumentParser.parse_args()

  create_repeat_files(args.species, args.repeats_file, args.output_folder)

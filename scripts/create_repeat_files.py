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
REPEAT_SUBLABELS = [""]*len(REPEAT_LABELS)
REPEATS_WITH_SUBLABELS = [
  "Satellite",
  "Satellite/Y-chromosome",
  "Satellite/acro",
  "Satellite/centr",
  "Satellite/subtelo",
  "Unspecified"
]

# Set sub-labels for "Unspecified". Per email from Bob H., there is also an “Unspecified” class
# that contains some subclasses that are satellites — they begin with ”SAT” and “StSat_pCHT”
REPEAT_SUBLABELS[REPEAT_LABELS.index("Unspecified")]=["SAT", "StSat_pCHT"]

# Set sub-labels for "Satellite/*"
REPEAT_SUBLABELS[REPEAT_LABELS.index("Satellite")]=[
  "BSR/Beta",
  "HSATII",
  "HSATI",
  "(CATTC)n",
  "(GAATG)n",
  "LSAU",
  "SAR",
  "SAT-VAR_rnd-1_family-9",
  "CER",
  "SATR1",
  "D20S16",
  "SATR2",
  "HSAT5",
  "PTPCHT7"
]
REPEAT_SUBLABELS[REPEAT_LABELS.index("Satellite/Y-chromosome")]=["ALRY-MAJOR_PT", "ALRY-MINOR_PT"]
REPEAT_SUBLABELS[REPEAT_LABELS.index("Satellite/acro")]=["6kbHsap", "ACRO1"]
REPEAT_SUBLABELS[REPEAT_LABELS.index("Satellite/centr")]=["SST1", "ALR/Alpha", "HSAT4", "GSATX", "GSATII", "GSAT"]
REPEAT_SUBLABELS[REPEAT_LABELS.index("Satellite/subtelo")]=["TAR1"]

CHROMOSOMES = ["chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10", "chr11", "chr12", "chr13", "chr14", "chr15", "chr16", "chr17", "chr18", "chr19", "chr20", "chr21", "chr22", "chr23", "chr24", "chrX", "chrY"]

def create_repeat_files(species, repeats_file, output_folder):
  repeats_df = pd.read_csv(repeats_file, sep="\s+", usecols=REPEATS_FILE_COLUMNS, names=REPEATS_COLUMN_NAMES)

  for index, label in enumerate(REPEAT_LABELS):
    for chromosome in CHROMOSOMES:
      sub_labels = REPEAT_SUBLABELS[index]
      print(f"label: <{label}>, sub_labels: <{sub_labels}>")

      if sub_labels == "":
        df_label = repeats_df[ (repeats_df.label == label) &
                               (repeats_df.chromosome.str.startswith(chromosome+"_")) ]
        output_file_path = path.join(output_folder, species, chromosome + "_" + label.replace("/", "_") + ".bed")
        df_label.to_csv(output_file_path, columns=["chromosome", "start", "stop"], header=False, index=False, sep="\t")
      else:
        for sub_label in sub_labels:
          df_label = repeats_df[ (repeats_df.label == label) &
                                 (repeats_df.sub_label.str.startswith(sub_label)) &
                                 (repeats_df.chromosome.str.startswith(chromosome+"_")) ]
          output_file_path = path.join(output_folder, species, chromosome + "_" + label.replace("/", "_") + "_" + sub_label.replace("/", "_") + ".bed")
          df_label.to_csv(output_file_path, columns=["chromosome", "start", "stop"], header=False, index=False, sep="\t")


def get_repeat_indexes():
  repeats_indexes = set()

  all_repeats_indexes = set(REPEAT_LABELS)
  repeats_with_sublabels_indexes = set(REPEATS_WITH_SUBLABELS)

  # Add all indexes for repeat types with no sublabels
  repeats_indexes.update(all_repeats_indexes.difference(repeats_with_sublabels_indexes))

  for repeat_with_sublabel in REPEATS_WITH_SUBLABELS:
    # Get sublabels
    sub_labels = REPEAT_SUBLABELS[REPEAT_LABELS.index(repeat_with_sublabel)]
    for sub_label in sub_labels:
      repeats_indexes.add(repeat_with_sublabel + "_" + sub_label)

  return repeats_indexes


if __name__ == "__main__":

  argumentParser = argparse.ArgumentParser("Create merged (no overlap) repeat files for a species, for each repeat/satellite type")

  argumentParser.add_argument("-s", "--species", type=str, required=True,
                              choices=["Bonobo", "Chimpanzee", "Human", "Gorilla", "B_Orangutan", "S_Orangutan", "Siamang"])
  argumentParser.add_argument("-f", "--repeats_file", type=str, required=True)
  argumentParser.add_argument("-o", "--output_folder", type=str, required=True)

  args = argumentParser.parse_args()

  create_repeat_files(args.species, args.repeats_file, args.output_folder)

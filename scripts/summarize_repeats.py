import argparse
import os
from os import path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from create_repeat_files import CHROMOSOMES as chromosomes
from create_repeat_files import REPEATS_FILE_COLUMNS, REPEATS_COLUMN_NAMES
from create_repeat_files import REPEAT_LABELS as repeat_types
from create_repeat_files import REPEAT_SUBLABELS as repeat_subtypes
from create_repeat_files import REPEATS_WITH_SUBLABELS as repeats_with_subtypes
from create_repeat_files import get_repeat_indexes

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

species_to_folder_dict = {
  "B_Orangutan": "Bornean",
  "Bonobo": "Bonobo",
  "Chimpanzee": "Chimpanzee",
  "Gorilla": "Gorilla",
  "Human": "CHM13v2.0_XY",
  "S_Orangutan": "Sumatran",
  "Siamang": "Siamang",
}

def summarize_repeats(species, repeats_folder, nbmst_output_folder, output_file):
  repeat_types_len = get_number_of_repeats(repeat_types, repeat_subtypes)
  zero_list = [0.00] * repeat_types_len
  data = {
    "APR": zero_list,
    "DR": zero_list,
    "GQ": zero_list,
    "IR": zero_list,
    "MR": zero_list,
    "STR": zero_list,
    "Z": zero_list,
  }

  repeats_length_sum = pd.Series(data=zero_list, index=get_repeat_indexes())
  intersect_length_sum = pd.DataFrame(data=data, index=get_repeat_indexes())

  # Populate repeat length Series. Add all chromosome values to the same cell.
  # We'd end up with repeat_types_len values
  for chromosome in chromosomes:
    for index, repeat_type in enumerate(repeat_types):
      if repeat_subtypes[index] == "":
        file_path = path.join(repeats_folder, species, "merged", chromosome + "_" + repeat_type.replace("/", "_") + "_merged.bed")

        try:
          df = pd.read_csv(file_path, sep="\t", names=["chr", "start", "stop"])
        except pd.errors.EmptyDataError:
          print(f"The TSV file {file_apth} is empty. No need to update repeats length series")
        except FileNotFoundError:
          print(f"The TSV file {file_path} does not exist")
        else:
          df["length"] = df["stop"] - df["start"] + 1
          repeats_length_sum.loc[repeat_type] += df["length"].sum()
      else:
        for repeat_subtype in repeat_subtypes[index]:
          file_path = path.join(repeats_folder, species, "merged", chromosome + "_" + repeat_type.replace("/", "_") + "_" + repeat_subtype.replace("/", "_") + "_merged.bed")

          try:
            df = pd.read_csv(file_path, sep="\t", names=["chr", "start", "stop"])
          except pd.errors.EmptyDataError:
            print(f"The TSV file {file_apth} is empty. No need to update repeats length series")
          except FileNotFoundError:
            print(f"The TSV file {file_path} does not exist")
          else:
            df["length"] = df["stop"] - df["start"] + 1
            repeats_length_sum.loc[repeat_type + "_" + repeat_subtype] += df["length"].sum()


  # Populate intersect length DataFrame. Add all chromosome values to the same cell.
  # We'd end up with repeat_types_len X len(non_b_dna_types) values
  for chromosome in chromosomes:
    for index, repeat_type in enumerate(repeat_types):
      for non_b_dna_type in non_b_dna_types:
        if repeat_subtypes[index] == "":
          file_path = path.join(repeats_folder, species, "intersect", chromosome + "_" + repeat_type.replace("/", "_") + "_intersect_" + non_b_dna_type + ".bed")
          try:
            df = pd.read_csv(file_path, sep="\t", names=["chr", "start", "stop"])
          except pd.errors.EmptyDataError:
            print(f"The TSV file {file_apth} is empty. No need to update repeats length series")
          except FileNotFoundError:
            print(f"The TSV file {file_path} does not exist")
          else:
            df["length"] = df["stop"] - df["start"] + 1
            intersect_length_sum.loc[repeat_type, non_b_dna_type] += df["length"].sum()
        else:
          for repeat_subtype in repeat_subtypes[index]:
            file_path = path.join(repeats_folder, species, "intersect", chromosome + "_" + repeat_type.replace("/", "_") + "_" + repeat_subtype.replace("/", "_") +  "_intersect_" + non_b_dna_type + ".bed")
            try:
              df = pd.read_csv(file_path, sep="\t", names=["chr", "start", "stop"])
            except pd.errors.EmptyDataError:
              print(f"The TSV file {file_apth} is empty. No need to update repeats length series")
            except FileNotFoundError:
              print(f"The TSV file {file_path} does not exist")
            else:
              df["length"] = df["stop"] - df["start"] + 1
              intersect_length_sum.loc[repeat_type + "_" + repeat_subtype, non_b_dna_type] += df["length"].sum()


  # Divide intersect length table rows by corresponding repeat length table values
  # This results in cell values beingbetween 0 and 1
  for index, repeat_type in enumerate(repeat_types):
    if repeat_subtypes[index] == "":
      if repeats_length_sum.loc[repeat_type] != 0.00:
        intersect_length_sum.loc[repeat_type] /= repeats_length_sum.loc[repeat_type]
    else:
      for repeat_subtype in repeat_subtypes[index]:
        if repeats_length_sum.loc[repeat_type + "_" + repeat_subtype] != 0.00:
          intersect_length_sum.loc[repeat_type + "_" + repeat_subtype] /= repeats_length_sum.loc[repeat_type + "_" + repeat_subtype]

  #
  # Add column with the number of repeat elements in each category, per species
  #
  repeats_file = path.join(repeats_folder, "input", species_to_folder_dict[species] + ".out")
  repeats_df = pd.read_csv(repeats_file, sep="\s+", usecols=REPEATS_FILE_COLUMNS, names=REPEATS_COLUMN_NAMES)
  repeats_df_no_subtype = repeats_df[~repeats_df.label.isin(repeats_with_subtypes)]
  number_of_repeat_types = repeats_df_no_subtype['label'].value_counts().sort_index()

  for repeat_with_subtype in repeats_with_subtypes:
    # We handle "Unspecified" separately below as we care about
    # sub_labels that startWith something (not equal to something)
    if repeat_with_subtype == "Unspecified":
      continue
    repeats_df_with_subtype = repeats_df[(repeats_df.label == repeat_with_subtype) & (repeats_df.sub_label.isin(repeat_subtypes[repeat_types.index(repeat_with_subtype)]))]
    label_plus_sublabel_series = repeats_df_with_subtype.loc[:, "label"].astype(str) + "_" + repeats_df_with_subtype.loc[:, "sub_label"].astype(str)
    number_of_repeat_subtypes_tmp = label_plus_sublabel_series.value_counts().sort_index()
    number_of_repeat_types = pd.concat([number_of_repeat_types, number_of_repeat_subtypes_tmp])

  # Add rows for Unspecified_SAT and Unspecified_StSat_pCHT to the number of repeat elements column
  repeats_df_sat = repeats_df[ (repeats_df['label'] == "Unspecified") & (repeats_df['sub_label'].str.startswith("SAT")) ]
  repeats_df_stsat = repeats_df[ (repeats_df['label'] == "Unspecified") & (repeats_df['sub_label'].str.startswith("StSat_pCHT")) ]
  number_of_repeat_types["Unspecified_SAT"] = repeats_df_sat.shape[0]
  number_of_repeat_types["Unspecified_StSat_pCHT"] = repeats_df_stsat.shape[0]
  number_of_repeat_types.sort_index(inplace=True)

  number_of_repeat_types = add_missing_indexes(number_of_repeat_types)
  number_of_repeat_types.sort_index(inplace=True)

  #
  # Add column with the length of the repeat elements in each category, per species
  #
  repeats_df_no_subtype_copy = repeats_df_no_subtype.copy()
  repeats_df_no_subtype_copy["length"] = repeats_df_no_subtype["stop"].astype(int) - repeats_df_no_subtype["start"].astype(int) + 1
  # Convert Dataframe to Series before passing it to add_missing_indexes
  length_of_repeat_types = repeats_df_no_subtype_copy[["label", "length"]].groupby("label").sum().T.squeeze().sort_index()

  for repeat_with_subtype in repeats_with_subtypes:
    # We handle "Unspecified" separately below as we care about
    # sub_labels that startWith something (not equal to something)
    if repeat_with_subtype == "Unspecified":
      continue
    repeats_df_with_subtype = repeats_df[(repeats_df.label == repeat_with_subtype) & (repeats_df.sub_label.isin(repeat_subtypes[repeat_types.index(repeat_with_subtype)]))]
    repeats_df_with_subtype_copy = repeats_df_with_subtype.copy()
    repeats_df_with_subtype_copy["length"] = repeats_df_with_subtype.loc[:, "stop"] - repeats_df_with_subtype.loc[:, "start"] + 1
    repeats_df_with_subtype_copy["label_plus_sublabel"] = repeats_df_with_subtype.loc[:, "label"].astype(str) + "_" + repeats_df_with_subtype.loc[:, "sub_label"].astype(str)

    length_of_repeat_subtypes_tmp = repeats_df_with_subtype_copy[["label_plus_sublabel", "length"]].groupby("label_plus_sublabel").sum().T.squeeze(axis=0).sort_index()
    length_of_repeat_types = pd.concat([length_of_repeat_types, length_of_repeat_subtypes_tmp])

  # Add rows for Unspecified_SAT and Unspecified_StSat_pCHT to the length of the repeat elements column
  repeats_df_sat_length = repeats_df_sat["stop"] - repeats_df_sat["start"] + 1
  repeats_df_stsat_length = repeats_df_stsat["stop"] - repeats_df_stsat["start"] + 1
  length_of_repeat_types.loc["Unspecified_SAT"] = repeats_df_sat_length.sum()
  length_of_repeat_types.loc["Unspecified_StSat_pCHT"] = repeats_df_stsat_length.sum()
  length_of_repeat_types.sort_index()

  length_of_repeat_types = add_missing_indexes(length_of_repeat_types)
  length_of_repeat_types.sort_index(inplace=True)

  #
  # Get the average non-B density per non-B type, per species
  # Divide dataframe cells by their corresponding non-B DNA density
  #   This allows us to detect enrichment, i.e., cases where density in a certain cell is higher than the non-B DNA density
  # Add non-B density per non-B type as a new row
  #
  average_non_b_dna_density = get_average_non_b_dna_density(nbmst_output_folder)
  average_non_b_dna_density_list = average_non_b_dna_density.tolist()
  print(f'average_non_b_dna_density_list: {average_non_b_dna_density_list}')

  average_non_b_dna_density_series = pd.Series(average_non_b_dna_density_list, index=intersect_length_sum.columns)
  intersect_length_sum_enrich = intersect_length_sum.div(average_non_b_dna_density_series)

  intersect_length_sum_enrich.sort_index(inplace=True)
  intersect_length_sum_enrich.loc["avg_non_b_dna_density"] = average_non_b_dna_density_list

  # Add new columns
  intersect_length_sum_enrich["number_of_repeat_types"] = number_of_repeat_types
  intersect_length_sum_enrich["length_of_repeat_types"] = length_of_repeat_types

  intersect_length_sum_enrich.to_csv(output_file, sep="\t", float_format="%.4f")

  # Generate heatmap and save to file
  heatmap_file_name = path.splitext(output_file)[0] + ".png"
  # Figure size in inches
  fig, ax = plt.subplots(figsize=(7.5, 20))
  sns.heatmap(intersect_length_sum_enrich.iloc[:-1,:-2], cbar=1, linewidths=2, square=True, cmap='Blues', annot=False)
  plt.savefig(heatmap_file_name)

def add_missing_indexes(repeat_types_series):
  existing_indexes = set(repeat_types_series.index.tolist())
  all_indexes = get_repeat_indexes()
  missing_indexes = all_indexes.difference(existing_indexes)

  print(f'len(missing_indexes): {len(missing_indexes)}')

  for missing_index in missing_indexes:
    print(f'Adding {missing_index}')
    repeat_types_series[missing_index] = 0.00

  return repeat_types_series


def get_average_non_b_dna_density(nbmst_output_folder):
  zero_list = [0.00] * len(non_b_dna_types)
  average_non_b_dna_density = pd.Series(data=zero_list, index=non_b_dna_types)
  total_length = 0

  # Read chr1 to chr24, and chrX and chrY lengths and add them to get total length
  for chromosome in chromosomes:
    chr_file_path = path.join(nbmst_output_folder, chromosome+".txt")

    try:
      df_chr = pd.read_csv(chr_file_path, sep="\t", names=["chr","length"])
    except pd.errors.EmptyDataError:
      print(f"The TSV file {chr_file_apth} is empty. No need to update total length series")
    except FileNotFoundError:
      print(f"The TSV file {chr_file_path} does not exist")

    total_length += df_chr["length"][0]

  # For each non-B DNA type, and for chr1 to chr24, and chrX and chrY,
  # add the non-B DNA total length to the series
  for non_b in non_b_dna_types:
    for chr in chromosomes:
      file_path = path.join(nbmst_output_folder, chr + "_" + non_b + ".bed")

      try:
        print(f"Reading {file_path}")
        non_b_df = pd.read_csv(file_path, sep="\t", usecols= [0,1,2], names=["chr", "start", "stop"])
      except pd.errors.EmptyDataError:
        print(f"The TSV file {file_apth} is empty. No need to update nonB DNA density series")
      except FileNotFoundError:
        print(f"The TSV file {file_path} does not exist")

      non_b_df["length"] = non_b_df["stop"] - non_b_df["start"]  + 1
      average_non_b_dna_density[non_b] += non_b_df["length"].sum()

  # Divide non-B DNA total length (for all chromosomes) by total length
  # (for all chromosomes), so non-B DNA total length is normalized
  print(f'total_length: {total_length}')
  print(f'average_non_b_dna_density: {average_non_b_dna_density}')
  print(f'average_non_b_dna_density.div(total_length): {average_non_b_dna_density.div(total_length)}')
  return average_non_b_dna_density.div(total_length)


def get_number_of_repeats(repeat_types, repeat_subtypes):
  number_of_repeats = 0

  for index, repeat_type in enumerate(repeat_types):
    if repeat_subtypes[index] == "":
      number_of_repeats += 1
    else:
      number_of_repeats += len(repeat_subtypes[index])

  return number_of_repeats


if __name__ == "__main__":
  argParser = argparse.ArgumentParser("This script summarizes nBMST results")

  argParser.add_argument("-s", "--species", type=str, required=True,
                         choices=["Bonobo", "Chimpanzee", "Human", "Gorilla", "B_Orangutan", "S_Orangutan", "Siamang"])
  argParser.add_argument("-f", "--repeats_folder", type=str, required=True)
  argParser.add_argument("-n", "--nbmst_output_folder", type=str, required=True)
  argParser.add_argument("-o", "--output_file", type=str, required=True)

  args = argParser.parse_args()

  summarize_repeats(args.species, args.repeats_folder, args.nbmst_output_folder, args.output_file)

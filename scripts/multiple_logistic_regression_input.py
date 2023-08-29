import argparse
from os import path

import pandas as pd

nb_list=["GQ", "MR", "STR", "APR", "IR", "DR", "Z"]

def concat_non_b_dna_files(non_b_dna_folder, species, chromosome):

  # Add the dataframe for the first non_b_dna file in full to df
  # For the remaining non_b_dna files, add only the dataframe's 'count' column to df
  first_file = True

  df = pd.DataFrame()

  # Read all chrX non-b DNA files and concatenate them, column wise to df
  for nb in nb_list:
    non_b_dna_file = path.join(non_b_dna_folder, species, species + "_" + chromosome + "_" + nb + "_density_final.bed")

    df_non_b_dna = pd.read_csv(non_b_dna_file, sep='\t')
    # This column is not needed. Drop it.
    df_non_b_dna.drop('chr', axis=1, inplace=True)
    # Rename column to avod clashing when joining with other dataframe
    df_non_b_dna.rename(columns={'count': nb + '_count'}, inplace=True)

    if first_file == True:
      df = pd.concat([df, df_non_b_dna], axis=1)
      first_file = False
    else:
      # Drop 'start' and 'stop' columns, so only 'count' column is concatenated
      df_non_b_dna.drop(columns=['start', 'stop'], inplace=True)
      df = pd.concat([df, df_non_b_dna], axis=1)

  return df

def create_multiple_logistic_regression_input(x_pre_existing_per_window_density_file,
                                              y_pre_existing_per_window_density_file,
                                              non_b_dna_folder, species, window_size,
                                              threshold, output_file):

  # Read all chrX non-b DNA files and concatenate them, column wise
  x_non_b_dna_density_df = concat_non_b_dna_files(non_b_dna_folder, species, "chrX")
  print(x_non_b_dna_density_df.shape)
  print(x_non_b_dna_density_df.head(3))

  # Read all chrY non-b DNA files and concatenate them, column wise
  y_non_b_dna_density_df = concat_non_b_dna_files(non_b_dna_folder, species, "chrY")
  print(y_non_b_dna_density_df.shape)
  print(y_non_b_dna_density_df.head(3))

  df_x = merge_input_files(x_pre_existing_per_window_density_file, x_non_b_dna_density_df,
                           window_size, threshold)
  df_y = merge_input_files(x_pre_existing_per_window_density_file, x_non_b_dna_density_df,
                           window_size, threshold)

  print(df_x.shape)
  print(df_x.head(3))
  print(df_y.shape)
  print(df_y.head(3))

  df = pd.concat([df_x, df_y])
  print(df.shape)
  print(df.head(3))
  print(df.tail(3))

  df.to_csv(output_file, index=False)


# Reads pre-existing and non-b DNA density files. Label novel column > threshold as True.
# Returns the merged file
def merge_input_files(pre_existing_per_window_density, non_b_dna_density_df,
                      window_size, threshold):

  df = pd.read_csv(pre_existing_per_window_density, sep='\t')
  # This column is not needed. Drop it.
  df.drop('chr', axis=1, inplace=True)
  # Rename column to avod clashing when joining with other dataframe
  df.rename(columns={'count': 'pre_existing_count'}, inplace=True)
  # To get the novel sequence percentage
  df['novel'] = (window_size - df['pre_existing_count']) / window_size
  # Mark rows with 'novel' greater than a threshold as 1
  # Mark rows with 'novel' less than a threshold as 0
  df['novel_label'] = df['novel'] > threshold
  df['novel_label'] = df['novel_label'].astype(int)

  df_merged = pd.merge(df, non_b_dna_density_df, how="inner", on=["start", "stop"])
  df_merged.drop(columns=["start", "stop", "novel", "pre_existing_count"], inplace=True)
  return df_merged


if __name__ == "__main__":
  argParser = argparse.ArgumentParser("Run Logistic Regression")
  argParser.add_argument("-x", "--x_pre_existing_per_window_density_file", type=str, required=True)
  argParser.add_argument("-y", "--y_pre_existing_per_window_density_file", type=str, required=True)
  argParser.add_argument("-b", "--non_b_dna_folder", type=str, required=True)
  argParser.add_argument("-s", "--species", type=str, required=True)
  argParser.add_argument("-z", "--window_size", type=int, required=True)
  argParser.add_argument("-t", "--threshold", type=float)
  argParser.add_argument("-o", "--output_file", type=str, required=True)
  args = argParser.parse_args()
  create_multiple_logistic_regression_input(args.x_pre_existing_per_window_density_file,
                                            args.y_pre_existing_per_window_density_file,
                                            args.non_b_dna_folder, args.species, args.window_size,
                                            args.threshold, args.output_file)

import argparse

import pandas as pd


def create_logistic_regression_input(x_pre_existing_per_window_density_file, x_non_b_dna_density_file,
                                     y_pre_existing_per_window_density_file, y_non_b_dna_density_file,
                                     window_size, threshold, output_file):
  df_x = merge_input_files(x_pre_existing_per_window_density_file, x_non_b_dna_density_file, window_size, threshold, output_file)
  df_y = merge_input_files(y_pre_existing_per_window_density_file, y_non_b_dna_density_file, window_size, threshold, output_file)

  print(df_x.shape)
  print(df_x.head())
  print(df_y.shape)
  print(df_y.head())

  df = pd.concat([df_x, df_y])
  print(df.shape)
  print(df.head(10))
  print(df.tail(10))

  df.to_csv(output_file, columns=["non_b_dna_count", "novel_label"], index=False)


# Reads pre-existing and non-b DNA density files. Label novel column > threshold as True.
# Returns the merged file
def merge_input_files(pre_existing_per_window_density, non_b_dna_density_file,
                      window_size, threshold, output_file):
  df = pd.read_csv(pre_existing_per_window_density, sep='\t')
  # This column is not needed. Drop it.
  df.drop('chr', axis=1, inplace=True)
  # Rename column to avoid clashing when joining with other dataframe
  df.rename(columns={'count': 'pre_existing_count'}, inplace=True)
  # To get the novel sequence percentage
  df['novel'] = (window_size - df['pre_existing_count']) / window_size
  # Mark rows with 'novel' greater than a threshold as 1
  # Mark rows with 'novel' less than a threshold as 0
  df['novel_label'] = df['novel'] > threshold
  df['novel_label'] = df['novel_label'].astype(int)

  df_non_b_dna = pd.read_csv(non_b_dna_density_file, sep='\t')
  # This column is not needed. Drop it.
  df_non_b_dna.drop('chr', axis=1, inplace=True)
  # Rename column to avod clashing when joining with other dataframe
  df_non_b_dna.rename(columns={'count': 'non_b_dna_count'}, inplace=True)

  df_merged = pd.merge(df, df_non_b_dna, how="inner", on=["start", "stop"])
  return df_merged


if __name__ == "__main__":
  argParser = argparse.ArgumentParser("Run Logistic Regression")
  argParser.add_argument("-x", "--x_pre_existing_per_window_density_file", type=str, required=True)
  argParser.add_argument("-a", "--x_non_b_dna_density_file", type=str, required=True)
  argParser.add_argument("-y", "--y_pre_existing_per_window_density_file", type=str, required=True)
  argParser.add_argument("-b", "--y_non_b_dna_density_file", type=str, required=True)
  argParser.add_argument("-s", "--window_size", type=int, required=True)
  argParser.add_argument("-t", "--threshold", type=float)
  argParser.add_argument("-o", "--output_file", type=str, required=True)
  args = argParser.parse_args()
  create_logistic_regression_input(args.x_pre_existing_per_window_density_file, args.x_non_b_dna_density_file,
                                   args.y_pre_existing_per_window_density_file, args.y_non_b_dna_density_file,
                                   args.window_size, args.threshold, args.output_file)

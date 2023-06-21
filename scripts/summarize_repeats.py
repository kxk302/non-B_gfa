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
  "Unspecified_SAT",
  "Unspecified_StSat_pCHT",
]


def summarize_repeats(species, repeats_folder, output_file):
  zero_list = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
  data = {
    "APR": zero_list,
    "DR": zero_list,
    "GQ": zero_list,
    "IR": zero_list,
    "MR": zero_list,
    "STR": zero_list,
    "Z": zero_list,
  }

  repeats_length_sum = pd.DataFrame(data=data, index=repeat_types)
  intersect_length_sum = pd.DataFrame(data=data, index=repeat_types)

  for chromosome in chromosomes:
    for repeat_type in repeat_types:
      pass

  for chromosome in chromosomes:
    for repeat_type in repeat_types:
      for non_b_dna_type in non_b_dna_types:
        pass


def summarize_single_nBMST(density_file_path, chromosome_name, chromosome_fatsa_file_path, species):

  df = pd.read_csv(density_file_path, sep="\t")
  
  length_sum = df['count'].sum()
  print(f'length_sum: {length_sum}')

  # Get the sequence length of the chromosome from the fasta file
  record_dict = IO.to_dict(IO.parse(chromosome_fatsa_file_path, "fasta"))
  chromosome_sequence_length = len(record_dict[chromosome_name].seq)
  print(f'{chromosome_name} sequence length: {chromosome_sequence_length}')

  length_sum_normalized = length_sum / chromosome_sequence_length
  print(f'length_sum_normalized: {length_sum_normalized}')

  return length_sum, length_sum_normalized 


def summarize_all_nBMST(nBMST_output_file_dir, chromosome_fasta_file_dir, output_file_dir):

  zero_list = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
  data = {
    "A-Phased Repeats": zero_list,
    "Short Tandem Repeats": zero_list,
    "Direct Repeats": zero_list,
    "Mirror Repeats": zero_list,
    "Inverted Repeats": zero_list,
    "G-Quadruplex": zero_list,
    "Z DNA": zero_list,
  }

  chrX_length_sum = pd.DataFrame(data=data, index=species_list_for_index)
  chrY_length_sum = pd.DataFrame(data=data, index=species_list_for_index)
  chrX_length_sum_normalized = pd.DataFrame(data=data, index=species_list_for_index)
  chrY_length_sum_normalized = pd.DataFrame(data=data, index=species_list_for_index)

  for chromosome in chromosomes:
    for species in species_list:
      for non_b_dna_type in non_b_dna_types:
        density_file_path = path.join(nBMST_output_file_dir, species, species + "_" + chromosome + "_" + non_b_dna_dict[non_b_dna_type] + "_density_final.bed" )
        print(f'density_file_path: {density_file_path}')

        chromosome_fatsa_file_path = path.join(chromosome_fasta_file_dir, species, "seqs_srcdir", chromosome + ".fa")
        print(f'chromosome_fatsa_file_path: {chromosome_fatsa_file_path}')

        length_sum, length_sum_normalized = summarize_single_nBMST(density_file_path, chromosome, 
                                                                   chromosome_fatsa_file_path, species)
        if chromosome == "chrX":
          chrX_length_sum.loc[species_dict[species], non_b_dna_type] = length_sum
          chrX_length_sum_normalized.loc[species_dict[species], non_b_dna_type] = length_sum_normalized
        else:
          chrY_length_sum.loc[species_dict[species], non_b_dna_type] = length_sum
          chrY_length_sum_normalized.loc[species_dict[species], non_b_dna_type] = length_sum_normalized
  
  chrX_length_sum.reset_index(inplace=True)
  chrX_length_sum = chrX_length_sum.rename(columns = {'index': 'Species'})
  chrX_length_sum.to_csv(output_file_dir + "/chrX.csv", float_format="%d", sep=",", index=False)

  chrX_length_sum_normalized.reset_index(inplace=True)
  chrX_length_sum_normalized = chrX_length_sum_normalized.rename(columns = {'index': 'Species'})
  chrX_length_sum_normalized.to_csv(output_file_dir + "/chrX_norm.csv", float_format="%.3f", sep=",", index=False)

  chrY_length_sum.reset_index(inplace=True)
  chrY_length_sum = chrY_length_sum.rename(columns = {'index': 'Species'})
  chrY_length_sum.to_csv(output_file_dir + "/chrY.csv", float_format="%d", sep=",", index=False)

  chrY_length_sum_normalized.reset_index(inplace=True)
  chrY_length_sum_normalized = chrY_length_sum_normalized.rename(columns = {'index': 'Species'})
  chrY_length_sum_normalized.to_csv(output_file_dir + "/chrY_norm.csv", float_format="%.3f", sep=",", index=False)


if __name__ == "__main__":
  argParser = argparse.ArgumentParser("This script summarizes nBMST results")

  argumentParser.add_argument("-s", "--species", type=str, required=True,
                              choices=["Bonobo", "Chimpanzee", "Human", "Gorilla", "B_Orangutan", "S_Orangutan", "Siamang"])
  argumentParser.add_argument("-f", "--repeats_folder", type=str, required=True)
  argumentParser.add_argument("-o", "--output_file", type=str, required=True)
  
  args = argParser.parse_args()
  
  summarize_repeats(args.species, args.repeats_folder, args.output_file)

import argparse
from os import path

import pandas as pd
import Bio.SeqIO as IO

species_list = ["Gorilla_gorilla", "Homo_sapiens", "Pan_paniscus", "Pan_troglodytes",
                "Pongo_abelii", "Pongo_pygmaeus", "Symphalangus_syndactylus"]

species_list_for_index = ["Gorilla", "Human", "Bonobo", "Chimpanzee",
                          "S. Orangutan", "B. Orangutan", "Siamang"]
species_dict = {
  "Gorilla_gorilla": "Gorilla",
  "Homo_sapiens" : "Human",
  "Pan_paniscus": "Bonobo",
  "Pan_troglodytes": "Chimpanzee",
  "Pongo_abelii": "S. Orangutan",
  "Pongo_pygmaeus": "B. Orangutan",
  "Symphalangus_syndactylus" : "Siamang",
}

non_b_dna_types = ["A-Phased Repeats", "Short Tandem Repeats", "Direct Repeats",
                   "Mirror Repeats", "Inverted Repeats", "G-Quadruplex", "Z DNA"]

chromosomes = ["chrX", "chrY"]

Homo_sapiens_chrX_index = "NC_060947.1 Homo sapiens isolate CHM13 chromosome X, alternate assembly T2T-CHM13v2.0"
Homo_sapiens_chrY_index = "NC_060948.1 Homo sapiens isolate NA24385 chromosome Y, alternate assembly T2T-CHM13v2.0"

non_b_dna_dict = {
    "A-Phased Repeats": "APR",
    "Short Tandem Repeats": "STR",
    "Direct Repeats": "DR",
    "Mirror Repeats": "MR",
    "Inverted Repeats": "IR",
    "G-Quadruplex": "GQ",
    "Z DNA": "Z",
  }

def summarize_single_nBMST(nBMST_output_file_path, chromosome_name,
                           chromosome_fatsa_file_path, species):

  df = pd.read_csv(nBMST_output_file_path, sep="\t", names=["chr", "start", "stop"])
  df["length"] = df["stop"] - df["start"] + 1
  length_sum = df["length"].sum()
  print(f'length_sum: {length_sum}')

  # Get the sequence length of the chromosome from the fasta file
  record_dict = IO.to_dict(IO.parse(chromosome_fatsa_file_path, "fasta"))
  chromosome_sequence_length = len(record_dict[chromosome_name].seq)
  print(f'{chromosome_name} sequence length: {chromosome_sequence_length}')

  length_sum_normalized = length_sum / chromosome_sequence_length
  print(f'length_sum_normalized: {length_sum_normalized}')

  return length_sum, length_sum_normalized


def summarize_all_nBMST(nBMST_output_file_dir, chromosome_fasta_file_dir, output_file_dir):

  zero_list = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
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
        nBMST_output_file_path = path.join(nBMST_output_file_dir, species, chromosome + "_" + non_b_dna_dict[non_b_dna_type] + "_merged.bed")
        print(f'nBMST_output_file_path: {nBMST_output_file_path}')

        chromosome_fatsa_file_path = path.join(chromosome_fasta_file_dir, species, "seqs_srcdir", chromosome + ".fa")
        print(f'chromosome_fatsa_file_path: {chromosome_fatsa_file_path}')

        length_sum, length_sum_normalized = summarize_single_nBMST(nBMST_output_file_path, chromosome,
                                                                   chromosome_fatsa_file_path, species)
        if chromosome == "chrX":
          chrX_length_sum.loc[species_dict[species], non_b_dna_type] = length_sum
          chrX_length_sum_normalized.loc[species_dict[species], non_b_dna_type] = length_sum_normalized
        else:
          chrY_length_sum.loc[species_dict[species], non_b_dna_type] = length_sum
          chrY_length_sum_normalized.loc[species_dict[species], non_b_dna_type] = length_sum_normalized

  chrX_length_sum.reset_index(inplace=True)
  chrX_length_sum = chrX_length_sum.rename(columns = {'index': 'Species'})
  chrX_length_sum.to_csv(output_file_dir + "/chrX.csv", float_format="%d", sep="&", index=False)

  chrX_length_sum_normalized.reset_index(inplace=True)
  chrX_length_sum_normalized = chrX_length_sum_normalized.rename(columns = {'index': 'Species'})
  chrX_length_sum_normalized.to_csv(output_file_dir + "/chrX_norm.csv", float_format="%.3f", sep="&", index=False)

  chrY_length_sum.reset_index(inplace=True)
  chrY_length_sum = chrY_length_sum.rename(columns = {'index': 'Species'})
  chrY_length_sum.to_csv(output_file_dir + "/chrY.csv", float_format="%d", sep="&", index=False)

  chrY_length_sum_normalized.reset_index(inplace=True)
  chrY_length_sum_normalized = chrY_length_sum_normalized.rename(columns = {'index': 'Species'})
  chrY_length_sum_normalized.to_csv(output_file_dir + "/chrY_norm.csv", float_format="%.3f", sep="&", index=False)


if __name__ == "__main__":
  argParser = argparse.ArgumentParser("This script summarizes nBMST results")

  argParser.add_argument("-n", "--nBMST_output_file_dir", type=str, required=True)
  argParser.add_argument("-c", "--chromosome_fasta_file_dir", type=str, required=True)
  argParser.add_argument("-o", "--output_file_dir", type=str, required=True)
  args = argParser.parse_args()

  summarize_all_nBMST(args.nBMST_output_file_dir, args.chromosome_fasta_file_dir, args.output_file_dir)

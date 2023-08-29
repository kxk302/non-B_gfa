import argparse

import Bio.SeqIO as IO


def get_chr_length(chromosome_fasta_file, chromosome_name, output_file):
  record_dict = IO.to_dict(IO.parse(chromosome_fasta_file, "fasta"))
  chromosome_sequence_length = len(record_dict[chromosome_name].seq)
  print(f'chrX sequence length: {chromosome_sequence_length}')
  with open(output_file, "w") as fp:
    fp.write(f'{chromosome_name}\t{chromosome_sequence_length}')


if __name__ == "__main__":
  argParser = argparse.ArgumentParser("This script returns the length of a chromosome given a fatsa file")

  argParser.add_argument("-i", "--chromosome_fasta_file", type=str, required=True)
  argParser.add_argument("-c", "--chromosome_name", type=str, required=True)
  argParser.add_argument("-o", "--output_file", type=str, required=True)
  args = argParser.parse_args()
  
  get_chr_length(args.chromosome_fasta_file, args.chromosome_name, args.output_file)

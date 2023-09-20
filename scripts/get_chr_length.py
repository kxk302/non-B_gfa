import argparse

import Bio.SeqIO as IO


def get_chr_length(chromosome_fasta_file, chromosome_name, file_extension):
  record_dict = IO.to_dict(IO.parse(chromosome_fasta_file, file_extension))
  if chromosome_name is None:
    chromosome_sequence_length = 0
    for value in record_dict.values():
      chromosome_sequence_length += len(value.seq)
    return chromosome_sequence_length
  else:
    chromosome_sequence_length = len(record_dict[chromosome_name].seq)
    return chromosome_sequence_length


if __name__ == "__main__":
  argParser = argparse.ArgumentParser("This script returns the length of a chromosome given a fatsa file")

  argParser.add_argument("-i", "--chromosome_fasta_file", type=str, required=True)
  argParser.add_argument("-c", "--chromosome_name", type=str)
  argParser.add_argument("-o", "--output_file", type=str, required=True)
  argParser.add_argument("-e", "--file_extension", type=str, default="fasta")
  args = argParser.parse_args()
  
  chromosome_sequence_length = get_chr_length(args.chromosome_fasta_file, args.chromosome_name, args.file_extension)
  print(f'chromosome sequence length: {chromosome_sequence_length}')
  with open(args.output_file, "w") as fp:
    if args.chromosome_name is None:
      fp.write(f'{chromosome_sequence_length}')
    else:
      fp.write(f'{args.chromosome_name}\t{chromosome_sequence_length}')

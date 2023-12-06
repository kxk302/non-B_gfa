import argparse
import re
from os import path

def split_fasta_file(fasta_file, output_dir, prefix):
  with open(fasta_file, 'r') as fp:
    fp_w = None

    for line in fp:
      # Extract chromosome idx from line starting with '>' and create a file to save chromosome sequence
      if line.startswith('>'):

        print(f"line: {line}")
        if fp_w is not None:
          # Close file pointer for previous line starting with '>'
          fp_w.close()

        # Skip header lines with 'random' in them
        # E.g., "chr1522_pat_hsa1421_random_utig4-145"
        if "random" in line:
          print(f"Skipping {line}")
          continue

        # findall returns a list, of size one for our case. Get the first element of the list
        under_score_index = line.find('_')
        chr_idx = line[:under_score_index]

        # Get chromosome index. E.g., get '22' from 'chr22'
        idx = chr_idx[len(prefix)+1:]
        print(f'Chromosome index: {idx}')

        # Create output file full path
        output_file_path = path.join(output_dir, f'chr{idx}.fa')

        # Open file to save chromosome sequence
        fp_w = open(output_file_path, 'w')
        fp_w.write(line)

      else:
        fp_w.write(line)


if __name__ == '__main__':
  argumentParser = argparse.ArgumentParser()
  argumentParser.add_argument('-f', '--fasta_file', help='Path to .fna file', type=str, required=True)
  argumentParser.add_argument('-o', '--output_dir', help='Output files directory', type=str, required=True)
  argumentParser.add_argument('-p', '--prefix', help='Prefix for chromosome header', type=str, default="chromosome")
  args = argumentParser.parse_args()

  split_fasta_file(args.fasta_file, args.output_dir, args.prefix)

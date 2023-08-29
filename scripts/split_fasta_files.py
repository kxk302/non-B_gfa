import argparse
import os
import pathlib
import shutil

chrX_prefix = ">chrX"
chrY_prefix = ">chrY"

def splitFastaFiles(input_folder, output_folder):
  files = os.listdir(input_folder)

  for file in files:
    file_path = os.path.join(input_folder, file)
    if os.path.isfile(file_path):
      file_name = pathlib.Path(file_path).stem 
      file_ext = pathlib.Path(file_path).suffix
      print(f"file_name: {file_name}, file_ext: {file_ext}")

      # Repeats validation files for humans already have chromosomes X and Y
      # specified in different files and there is no need to split them. If the 
      # file name starts with "CHM13" or "HG002", they are human files and
      # we just need to copy them as is to the output_folder
      if file_name.startswith("CHM13") or file_name.startswith("HG002"):
        shutil.copy(file_path, os.path.join(output_folder, file_name+file_ext))
      else:

        # Create 2 new files to save chrX and chrY reads into
        # Append file name with ".chrX" and ".chrY"
        chrX_file_path = os.path.join(output_folder, file_name + ".chrX" + file_ext)
        chrY_file_path = os.path.join(output_folder, file_name + ".chrY" + file_ext)
        print(f"chrX_file_path: {chrX_file_path}")
        print(f"chrY_file_path: {chrY_file_path}")

        with open(file_path, "r") as in_fp, open(chrX_file_path, "w") as x_fp, open(chrY_file_path, "w") as y_fp:
          while True:
            line1 = in_fp.readline()
            line2 = in_fp.readline()
          
            if not line1 or not line2:
              print(f"Reached the end of file {file_path}")
              break

            if line1.startswith(chrX_prefix):
              x_fp.write(line1)
              x_fp.write(line2)
            if line1.startswith(chrY_prefix):
              y_fp.write(line1)
              y_fp.write(line2)


if __name__ == "__main__":
  argParse = argparse.ArgumentParser("Split Fasta file into two fasta files based on X and Y chromosomes")

  argParse.add_argument("-i", "--input_folder", type=str, required=True)
  argParse.add_argument("-o", "--output_folder", type=str, required=True)

  args= argParse.parse_args()
  splitFastaFiles(args.input_folder, args.output_folder)

import argparse
import pathlib
import os
import subprocess


def run_nBMST(input_folder, output_folder, input_file_extension):
  files = os.listdir(input_folder)

  for file in files:
    print(f"file: {file}")
    file_path = os.path.join(input_folder, file)

    # Skip directories
    if not os.path.isfile(file_path):
      continue

    file_name = pathlib.Path(file_path).stem
    file_extensions = pathlib.Path(file_path).suffixes
    file_extension = pathlib.Path(file_path).suffix

    if file_extension != input_file_extension:
      continue

    species = file_name.split("_")[0]
    print(f"species: {species}")

    repeat_type = file_extensions[-3].replace(".", "")
    print(f"repeat_type: {repeat_type}")

    chromosome_type = file_extensions[-2].replace(".", "")
    print(f"chromosome_type: {chromosome_type}")


    OutputFilePrefix = species + "-" + chromosome_type + "-" + repeat_type

    # We run Quadron for G4 annotation. Hence, skip G4 here
    result = subprocess.run(["./gfa", "-seq", file_path, "-out", OutputFilePrefix, "-skipGQ"])
    print(f"result: {result}")

    # Move nBMST output files from current directory to output_folder
    result = subprocess.run(["find", ".", "-maxdepth", "1", "-iname", OutputFilePrefix + "_*",\
                             "-exec", "mv", "{}", output_folder, ";"])
    print(f"result: {result}")


if __name__ == "__main__":
  argParse = argparse.ArgumentParser("Run nBMST on repeats validation files")

  argParse.add_argument("-i", "--input_folder", type=str, required=True)
  argParse.add_argument("-o", "--output_folder", type=str, required=True)
  argParse.add_argument("-e", "--input_file_extension", type=str, default="fasta")

  args = argParse.parse_args()
  run_nBMST(args.input_folder, args.output_folder, args.input_file_extension)

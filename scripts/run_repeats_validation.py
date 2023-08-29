import argparse
import pathlib
import os
import subprocess


def run_nBMST(input_folder, output_folder):
  files = os.listdir(input_folder)

  for file in files:
    print(f"file: {file}")
    file_path = os.path.join(input_folder, file)

    if os.path.isfile(file_path):
      file_name = pathlib.Path(file_path).stem
      file_extensions = pathlib.Path(file_path).suffixes

      species = file_name.split("_")[0]
      print(f"species: {species}")

      repeat_type = file_extensions[-3].replace(".", "")
      print(f"repeat_type: {repeat_type}")

      chromosome_type = file_extensions[-2].replace(".", "")
      print(f"chromosome_type: {chromosome_type}")

      # ./gfa -seq $InputFastaFile -out $OutputFilePrefix
      # find . -maxdepth 1 -iname "${OutputFilePrefix}_*" -exec mv {} ${OutputDir} \;

      OutputFilePrefix = species + "-" + chromosome_type + "-" + repeat_type
      #result = subprocess.run(["./gfa", "-seq", file_path, "-out", OutputFilePrefix]) 
      #print(f"result: {result}")

      result = subprocess.run(["find", ".", "-maxdepth", "1", "-iname", OutputFilePrefix + "_*",\
                               "-exec", "mv", "{}", output_folder, ";"])
      print(f"result: {result}")


if __name__ == "__main__":
  argParse = argparse.ArgumentParser("Run nBMST on repeats validation files")

  argParse.add_argument("-i", "--input_folder", type=str, required=True)
  argParse.add_argument("-o", "--output_folder", type=str, required=True)

  args = argParse.parse_args()
  run_nBMST(args.input_folder, args.output_folder)



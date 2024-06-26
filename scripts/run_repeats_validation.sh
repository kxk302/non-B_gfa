#!/bin/bash

if [$# -ne 3]; then
  echo "Incorrect number of parameters"
  echo "Specify the input folder, output folder, and input file extension"
  exit
fi

InputFolder=${1:-"./repeats/validation_input/split_fasta_files"}
OutputFolder=${2:-"./repeats/validation_output/"}
InputFileExtension=${3:-".fasta"}

echo "InputFolder: <$InputFolder>"
echo "OutputFolder <$OutputFolder>"
echo "InputFileExtension <$InputFileExtension>"

python3 ./scripts/run_repeats_validation.py -i $InputFolder -o $OutputFolder -e $InputFileExtension

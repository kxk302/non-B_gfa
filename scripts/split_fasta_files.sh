#!/bin/bash

if [$# -ne 2]; then
  echo "Incorrect number of parameters"
  echo "Specify the input and output folder"
  exit
fi

InputFolder=${1:-"./repeats/validation_input/"}
OutputFolder=${2:-"./repeats/validation_input/split_fasta_files/"}

echo "InputFolder: <$InputFolder>"
echo "OutputFolder <$OutputFolder>"

python3 ./scripts/split_fasta_files.py -i $InputFolder -o $OutputFolder

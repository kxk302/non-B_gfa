#!/bin/bash

if [$# -ne 3]; then
  echo "Incorrect number of parameters"
  echo "Specify the input folder, output folder, and input file extension"
  exit
fi

InputFolder=${1:-"/Users/kxk302/workspace/Quadron_Docker/input/hg19"}
OutputFolder=${2:-"/Users/kxk302/workspace/Quadron_Docker/output/hg19/nBMST"}
InputFileExtension=${3:-".fa"}

echo "InputFolder: <$InputFolder>"
echo "OutputFolder <$OutputFolder>"
echo "InputFileExtension <$InputFileExtension>"

python3 ./scripts/run_hg19.py -i $InputFolder -o $OutputFolder -e $InputFileExtension

#!/bin/bash

if [ $# -ne 2 ];then
  echo "Incorrect number of parameters"
  echo "Specify the input and output folders"
  exit
fi

InputFolder=$1
OutputFolder=$2

echo "InputFolder: <$InputFolder>"
echo "OutputFolder: <$OutputFolder>"

for file in $(ls ${InputFolder}/*.tsv)
do
  echo "file: <$file>"
  python3 scripts/convert_nBMST_output_to_bed.py -i $file -o $OutputFolder
done



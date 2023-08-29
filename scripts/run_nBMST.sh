#!/bin/bash

if [ $# -ne 3 ]; then
    echo "Incorrect number of parameters"
    echo "Specify the input fasta file, the output file name prefix, and the output diectory"
    exit
fi

InputFastaFile=$1
OutputFilePrefix=$2
OutputDir=$3

echo "InputFastaFile: <$InputFastaFile>"
echo "OutputFilePrefix <$OutputFilePrefix>"
echo "OutputDir <$OutputDir>"

./gfa -seq $InputFastaFile -out $OutputFilePrefix
find . -maxdepth 1 -iname "${OutputFilePrefix}_*" -exec mv {} ${OutputDir} \;


#!/bin/bash

# To run this script, must activate the venv via the following command:
# `. ./venv/bin/activate`

if [ $# -ne 1 ]
then
    echo "Incorrect number of parameters"
    echo "Specify the path to multi fasta file"
    exit
fi

multi_fatsa_file=$1

# The output of this command is in the current directory
# Move the .fasta files as you see fit 
faidx --split-files ${multi_fatsa_file}

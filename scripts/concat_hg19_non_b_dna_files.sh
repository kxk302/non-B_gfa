#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Incorrect number of parameters"
    echo "Specify the nBMST .bed folder"
    exit
fi

NbmstBedFolder=$1

echo "NbmstBedFolder: <$NbmstBedFolder>"

hg19_chromosomes="chr10 chr11 chr12 chr13 chr14 chr15 chr16 chr17 chr18 chr19 chr1 chr20 chr21 chr22 chr2 chr3 chr4 chr5 chr6 chr7 chr8 chr9 chrX chrY"

for chromosome in ${hg19_chromosomes}
do
  python3 ./scripts/concat_non_b_dna_files.py -i ${NbmstBedFolder} -o ${NbmstBedFolder}/${chromosome}_all.bed -c ${chromosome} -e ".bed" -s Z APR;
done

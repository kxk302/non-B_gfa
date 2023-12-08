#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Incorrect number of parameters"
    echo "Specify the nBMST output folder, and the spacer length filter value"
    exit
fi

NbmstOutputFolder=$1
SpacerLength=$2

echo "NbmstOutputFolder: <$NbmstOutputFolder>"
echo "SpacerLength: <$SpacerLength>"

for species in "Gorilla_gorilla" "Pan_paniscus" "Pongo_abelii" "Symphalangus_syndactylus" "Homo_sapiens" "Pan_troglodytes" "Pongo_pygmaeus"
do
  for chr in "chr1" "chr2" "chr3" "chr4" "chr5" "chr6" "chr7" "chr8" "chr9" "chr10" "chr11" "chr12" "chr13" "chr14" "chr15" "chr16" "chr17" "chr18" "chr19" "chr20" "chr21" "chr22" "chr23" "chr24" "chrX" "chrY"
  do
    for non_b in "DR" "IR" "MR"
    do
      if [ -e ${NbmstOutputFolder}/${species}/backup/${chr}_${non_b}.tsv ]
      then
        python3 ./scripts/filter.py -n ${NbmstOutputFolder}/${species}/backup/${chr}_${non_b}.tsv -f $SpacerLength -o ${NbmstOutputFolder}/${species}/${chr}_${non_b}.tsv
      fi
    done
  done
done

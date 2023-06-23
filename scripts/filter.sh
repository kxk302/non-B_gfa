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
  for chr in "chrX" "chrY"
  do
    for non_b in "DR" "IR" "MR"
    do
      python3 ./scripts/filter.py -n ${NbmstOutputFolder}/${species}/backup/${chr}_${non_b}.tsv -f $SpacerLength -o ${NbmstOutputFolder}/${species}/${chr}_${non_b}.tsv
    done
  done
done

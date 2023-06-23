#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Incorrect number of parameters"
    echo "Specify the nBMST output folder"
    exit
fi

NbmstOutputFolder=$1

echo "NbmstOutputFolder: <$NbmstOutputFolder>"

for species in "Gorilla_gorilla" "Pan_paniscus" "Pongo_abelii" "Symphalangus_syndactylus" "Homo_sapiens" "Pan_troglodytes" "Pongo_pygmaeus"
do
  cd $NbmstOutputFolder/$species
  mkdir -p backup
  for chr in "chrX" "chrY"
  do
    for non_b in "DR" "IR" "MR"
    do
      cp ${chr}_${non_b}.tsv ./backup
    done
  done
  cd -
done

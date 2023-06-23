#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Incorrect number of parameters"
    echo "Specify the nBMST output folder"
    exit
fi

NbmstOutputFolder=$1

echo "NbmstOutputFolder: <$NbmstOutputFolder>"

nb_list="GQ MR STR APR IR DR Z"

for species in "Gorilla_gorilla" "Pan_paniscus" "Pongo_abelii" "Symphalangus_syndactylus" "Homo_sapiens" "Pan_troglodytes" "Pongo_pygmaeus"
do
  for chr in "chrX" "chrY"
  do
    python3 ./scripts/concat_non_b_dna_files.py -i ${NbmstOutputFolder}/${species}/ -o ${NbmstOutputFolder}/${species}/${chr}_all.bed -c ${chr};
    for non_b in ${nb_list}
    do
      python3 ./scripts/concat_non_b_dna_files.py -i ${NbmstOutputFolder}/${species}/ -o ${NbmstOutputFolder}/${species}/${chr}_${non_b}.bed -c ${chr} -n ${non_b};
    done
  done
done

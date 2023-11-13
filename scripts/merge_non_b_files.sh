#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Incorrect number of parameters"
    echo "Specify the nBMST output folder"
    exit
fi

NbmstOutputFolder=$1
echo "NbmstOutputFolder: <$NbmstOutputFolder>"

cd $NbmstOutputFolder

species_list="Gorilla_gorilla Pan_paniscus Pongo_abelii Symphalangus_syndactylus Homo_sapiens Pan_troglodytes Pongo_pygmaeus"
nb_list="GQ MR STR APR IR DR Z all"
chr_list="chrX chrY"

for folder in $species_list
do
  cd $folder;
  for non_b in $nb_list
  do
    for chr in $chr_list
    do
      file=${chr}_${non_b}.bed
      bedtools merge -i ${file} > "${file/.bed/_merged.bed}"
    done
  done
  cd -;
done

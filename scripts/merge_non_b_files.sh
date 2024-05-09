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
chr_list="chr1 chr2 chr3 chr4 chr5 chr6 chr7 chr8 chr9 chr10 chr11 chr12 chr13 chr14 chr15 chr16 chr17 chr18 chr19 chr20 chr21 chr22 chr23 chr24 chrX chrY"

for folder in $species_list
do
  cd $folder;
  for non_b in $nb_list
  do
    for chr in $chr_list
    do
      file=${chr}_${non_b}.bed
      if [ -e ${file} ]
      then
        bedtools merge -i ${file} > "${file/.bed/_merged.bed}"
      fi
    done
  done
  cd -;
done

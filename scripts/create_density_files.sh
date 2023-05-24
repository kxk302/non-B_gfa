#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Incorrect number of parameters"
    echo "Specify the species folder, and the species"
    exit
fi

SpeciesFolder=$1
Species=$2

echo "SpeciesFolder: <$SpeciesFolder>"
echo "Species: <$Species>"

nb_list="GQ MR STR APR IR DR Z"
chr_list="chrX chrY"

for nb in $nb_list; do
  for chr in $chr_list; do
    cmd_1="bedtools coverage -a ${SpeciesFolder}/${chr}_100k_windows.bed -b ${SpeciesFolder}/${chr}_${nb}.bed -d"
    echo $cmd_1
    $cmd_1 > ${SpeciesFolder}/${chr}_${nb}_density.bed

    cmd_2="python3 ./scripts/create_density_files.py -i ${SpeciesFolder}/${chr}_${nb}_density.bed -o ${SpeciesFolder}/${Species}_${chr}_${nb}_density_final.bed -c ${chr}"
    echo $cmd_2
    $cmd_2
  done
done


#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Incorrect number of parameters"
    echo "Specify the species folder, and the chromosome name"
    exit
fi

SpeciesFolder=$1
Chromosome=$2

echo "SpeciesFolder: <$SpeciesFolder>"
echo "Chromosome: <$Chromosome>"

nb_list="GQ MR STR APR IR DR Z"

for nb in $nb_list; do
  cmd="python3 ./scripts/concat_non_b_dna_files.py -i ${SpeciesFolder}/ -o ${SpeciesFolder}/${Chromosome}_${nb}.bed -c ${Chromosome} -n ${nb}"
  echo $cmd
  $cmd
done


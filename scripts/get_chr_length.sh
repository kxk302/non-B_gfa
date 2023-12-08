#!/bin/bash

input_folder=${1:-"./input"}
output_folder=${2:-"./output"}

#for species in "Gorilla_gorilla" "Pan_paniscus" "Pongo_abelii" "Symphalangus_syndactylus" "Homo_sapiens" "Pan_troglodytes" "Pongo_pygmaeus"
for species in "Gorilla_gorilla" "Pan_paniscus" "Symphalangus_syndactylus" "Pan_troglodytes" "Pongo_pygmaeus"
do
  for chr in "chrX" "chrY" "chr1" "chr2" "chr3" "chr4" "chr5" "chr6" "chr7" "chr8" "chr9" "chr10" "chr11" "chr12" "chr13" "chr14" "chr15" "chr16" "chr17" "chr18" "chr19" "chr20" "chr21" "chr22" "chr23" "chr24"
  do
    input_file="${input_folder}/${species}/seqs_srcdir/${chr}.fa"
    if [ -e ${input_file} ]
    then
      cmd="python3 ./scripts/get_chr_length.py -i ${input_file} -c ${chr} -o ${output_folder}/$species/${chr}.txt"
      echo "$cmd"
      $cmd
    fi
  done
done



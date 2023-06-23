#!/bin/bash

for species in "Gorilla_gorilla" "Pan_paniscus" "Pongo_abelii" "Symphalangus_syndactylus" "Homo_sapiens" "Pan_troglodytes" "Pongo_pygmaeus"
do
  for chr in "chrX" "chrY"
  do
    cmd="python3 ./scripts/get_chr_length.py -i ./input/${species}/seqs_srcdir/${chr}.fa -c ${chr} -o ./output/$species/${chr}.txt"
    echo "$cmd"
    $cmd
  done
done



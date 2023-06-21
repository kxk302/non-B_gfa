#!/bin/bash

species_list="Gorilla_gorilla Pan_paniscus Pongo_abelii Homo_sapiens Pan_troglodytes"
nb_list="all GQ MR STR APR IR DR Z"

for species in ${species_list}
do
  for nb in $nb_list
  do
    cmd="python3 ./scripts/logistic_regression_input.py -x ./output/${species}/chrX_pre_existing_per_window_density.bed -a ./output/${species}/${species}_chrX_${nb}_density_final.bed -y ./output/${species}/chrY_pre_existing_per_window_density.bed -b ./output/${species}/${species}_chrY_${nb}_density_final.bed -s 100000 -t 0.00 -o ./output/${species}/${species}_logistic_regression_${nb}_input.csv"
    $cmd
  done
done

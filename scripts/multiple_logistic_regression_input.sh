#!/bin/bash

species_list="Gorilla_gorilla Pan_paniscus Pongo_abelii Homo_sapiens Pan_troglodytes"

for species in ${species_list}
do
  python3 ./scripts/multiple_logistic_regression_input.py -x ./output/${species}/chrX_pre_existing_per_window_density.bed -y ./output/${species}/chrY_pre_existing_per_window_density.bed -b ./output/ -s ${species} -z 100000 -t 0.00 -o ./output/${species}/${species}_multiple_logistic_regression_input.csv
done


#!/bin/bash

species_list="Gorilla_gorilla Pan_paniscus Pongo_abelii Homo_sapiens Pan_troglodytes"
nb_list="all GQ MR STR APR IR DR Z"

for species in ${species_list}
do
  for nb in ${nb_list}
  do
    Rscript ./scripts/logistic_regression.R ./output/${species}/${species}_logistic_regression_${nb}_input.csv ./output/${species}/${species}_logistic_regression_${nb}_ouput.txt
  done
done


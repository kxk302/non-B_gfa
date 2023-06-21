#!/bin/bash

species_list="Gorilla_gorilla Pan_paniscus Pongo_abelii Homo_sapiens Pan_troglodytes"

for species in ${species_list}
do
  Rscript ./scripts/multiple_logistic_regression.R ./output/${species}/${species}_multiple_logistic_regression_input.csv ./output/${species}/${species}_multiple_logistic_regression_ouput.txt
done


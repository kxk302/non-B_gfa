#!/bin/bash

species_list="Gorilla_gorilla Homo_sapiens Pan_paniscus Pan_troglodytes Pongo_abelii Pongo_pygmaeus Symphalangus_syndactylus"
chr_list="chrX chrY"

for species in ${species_list}
do
  for chr in ${chr_list}
  do
    ./scripts/run_nBMST.sh ./input/${species}/seqs_srcdir/${chr}.fa ${chr} ./output/${species}
  done
done

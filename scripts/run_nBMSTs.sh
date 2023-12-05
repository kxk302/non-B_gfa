#!/bin/bash

input_dir=${1:-"."}
output_dir=${2:-"."}

species_list="Gorilla_gorilla Pan_paniscus Pan_troglodytes Pongo_abelii Pongo_pygmaeus Symphalangus_syndactylus"
chr_list="1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 X Y"

for species in ${species_list}
do
  for chr in ${chr_list}
  do
    fasta_file="${input_dir}/input/${species}/seqs_srcdir/chr${chr}.fa"
    echo "fasta_file: ${fasta_file}"
    if [ -e ${fasta_file} ];then
      ./scripts/run_nBMST.sh ${fasta_file} ${chr} ${output_dir}/output/${species}
    fi
  done
done

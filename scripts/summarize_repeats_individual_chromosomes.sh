#!/usr/local/bin/bash

species_list="B_Orangutan Bonobo Chimpanzee Gorilla Human S_Orangutan Siamang"

chr_list="chr1 chr2 chr3 chr4 chr5 chr6 chr7 chr8 chr9 chr10 chr11 chr12 chr13 chr14 chr15 chr16 chr17 chr18 chr19 chr20 chr21 chr22 chr23 chr24 chrX chrY"

# Dictionary to go from one species acronym to another
declare -A species_map
species_map=(["B_Orangutan"]="Pongo_pygmaeus" ["Bonobo"]="Pan_paniscus"  ["Chimpanzee"]="Pan_troglodytes" ["Gorilla"]="Gorilla_gorilla" ["Human"]="Homo_sapiens" ["S_Orangutan"]="Pongo_abelii" ["Siamang"]="Symphalangus_syndactylus")

for species in $species_list
do
  for chr in $chr_list
  do
   python3 ./scripts/summarize_repeats.py -s ${species} -f ./repeats/ -o ./repeats/summary_output/${species}/${species}_${chr}_repeats_summary.tsv -n ./v2/output/${species_map[${species}]} -c ${chr}
  done
done

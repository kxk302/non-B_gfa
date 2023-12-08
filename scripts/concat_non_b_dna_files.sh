#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Incorrect number of parameters"
    echo "Specify the nBMST output folder"
    exit
fi

NbmstOutputFolder=$1

echo "NbmstOutputFolder: <$NbmstOutputFolder>"

nb_list="GQ MR STR APR IR DR Z"

for species in "Gorilla_gorilla" "Pan_paniscus" "Pongo_abelii" "Symphalangus_syndactylus" "Homo_sapiens" "Pan_troglodytes" "Pongo_pygmaeus"
do
  for chr in "chr1" "chr2" "chr3" "chr4" "chr5" "chr6" "chr7" "chr8" "chr9" "chr10" "chr11" "chr12" "chr13" "chr14" "chr15" "chr16" "chr17" "chr18" "chr19" "chr20" "chr21" "chr22" "chr23" "chr24" "chrX" "chrY"
  do
    python3 ./scripts/concat_non_b_dna_files.py -i ${NbmstOutputFolder}/${species}/ -o ${NbmstOutputFolder}/${species}/${chr}_all.bed -c ${chr};
    for non_b in ${nb_list}
    do
      python3 ./scripts/concat_non_b_dna_files.py -i ${NbmstOutputFolder}/${species}/ -o ${NbmstOutputFolder}/${species}/${chr}_${non_b}.bed -c ${chr} -n ${non_b};
    done
  done
done

#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Incorrect number of parameters"
    echo "Specify the nBMST output folder"
    exit
fi

NbmstOutputFolder=$1

echo "NbmstOutputFolder: <$NbmstOutputFolder>"

nb_list="GQ MR STR APR IR DR Z"
chr_list="chrX chrY"
species_list="Gorilla_gorilla Pan_paniscus Pongo_abelii Symphalangus_syndactylus Homo_sapiens Pan_troglodytes Pongo_pygmaeus"

for species in $species_list
do
  cd ${NbmstOutputFolder}/${species}
  for chr in $chr_list
  do
    # Create density files for all non-b DNAs combined
    cmd_1="bedtools coverage -a ${chr}_100k_windows.bed -b ${chr}_all.bed -d"
    echo $cmd_1
    $cmd_1 > ${chr}_all_density.bed

    for nb in $nb_list
    do
      # Create density files for each non-b DNA
      cmd_1="bedtools coverage -a ${chr}_100k_windows.bed -b ${chr}_${nb}.bed -d"
      echo $cmd_1
      $cmd_1 > ${chr}_${nb}_density.bed
    done
  done
  cd -
done

# Aggregate denisty files into its final form
for species in $species_list
do
  for chr in $chr_list
  do
    # Aggregate density files for all non-b DNAs combined
    python3 ./scripts/create_density_files.py -i ${NbmstOutputFolder}/${species}/${chr}_all_density.bed -o ${NbmstOutputFolder}/${species}/${species}_${chr}_all_density_final.bed -c ${chr};

    for nb in $nb_list
    do
      # Aggregate density files for each non-b DNA
      python3 ./scripts/create_density_files.py -i ${NbmstOutputFolder}/${species}/${chr}_${nb}_density.bed -o ${NbmstOutputFolder}/${species}/${species}_${chr}_${nb}_density_final.bed -c ${chr};
    done
  done
done

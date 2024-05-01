#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Incorrect number of parameters"
    echo "Specify the nBMST output folder, and window size"
    exit
fi

NbmstOutputFolder=$1
WindowSize=$2

WindowSizeK=$((WindowSize/1000))

echo "NbmstOutputFolder: <$NbmstOutputFolder>"
echo "WindowSize: <$WindowSize>"
echo "WindowSizeK: <$WindowSizeK>"

for species in "Gorilla_gorilla" "Pan_paniscus" "Pongo_abelii" "Symphalangus_syndactylus" "Homo_sapiens" "Pan_troglodytes" "Pongo_pygmaeus"
do
  cd $NbmstOutputFolder/$species
  for chr in "chr1" "chr2" "chr3" "chr4" "chr5" "chr6" "chr7" "chr8" "chr9" "chr10" "chr11" "chr12" "chr13" "chr14" "chr15" "chr16" "chr17" "chr18" "chr19" "chr20" "chr21" "chr22" "chr23" "chr24" "chrX" "chrY"
  do
    if [ -e ${chr}.txt ]
    then
      bedtools makewindows -g ${chr}.txt -w ${WindowSize} > ${chr}_${WindowSizeK}k_windows.bed;
    fi
  done
  cd -
done

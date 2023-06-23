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
  for chr in "chrX" "chrY"
  do
    bedtools makewindows -g ${chr}.txt -w ${WindowSize} > ${chr}_${WindowSizeK}k_windows.bed;
  done
  cd -
done

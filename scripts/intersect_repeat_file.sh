#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Incorrect number of parameters"
    echo "Specify the repeats folder, and the non-B DNA annotations folder"
    exit
fi

RepeatsFolder=$1
NonBDNAFolder=$2

echo "RepeatsFolder: <$RepeatsFolder>"
echo "NonBDNAFolder: <$NonBDNAFolder>"

cd $RepeatsFolder
mkdir -p intersect
cd merged

for chr in "chr1" "chr2" "chr3" "chr4" "chr5" "chr6" "chr7" "chr8" "chr9" "chr10" "chr11" "chr12" "chr13" "chr14" "chr15" "chr16" "chr17" "chr18" "chr19" "chr20" "chr21" "chr22" "chr23" "chr24" "chrX" "chrY"
do
  for repeat in $(ls ${chr}_*_merged.bed)
  do
    for nonB in "APR" "DR" "GQ" "IR" "MR" "STR" "Z"
    do
      # Create an empty output file. The command below will populate it. This makes sure an
      # output file is created even if the command below produces no output
      touch ../intersect/${repeat/_merged.bed/_intersect_${nonB}.bed}
      cmd="bedtools intersect -a ${repeat} -b ${NonBDNAFolder}/${chr}_${nonB}_merged.bed > ../intersect/${repeat/_merged.bed/_intersect_${nonB}.bed}"
      echo "cmd: $cmd"
      eval "$cmd"
    done
  done
done

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

for chr in "chrX" "chrY"
do
  for repeat in $(ls $chr*_merged.bed)
  do
    for nonB in "APR" "DR" "GQ" "IR" "MR" "STR" "Z"
    do
      bedtools intersect -a $repeat -b ${NonBDNAFolder}/${chr}_${nonB}.bed > ${repeat/_merged.bed/_intersect_$nonB.bed}
    done
  done
done

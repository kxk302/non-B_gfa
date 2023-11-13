#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Incorrect number of parameters"
    echo "Specify the nBMST output folder"
    exit
fi

NbmstOutputFolder=$1
echo "NbmstOutputFolder: <$NbmstOutputFolder>"

cd $NbmstOutputFolder

nb_list="GQ MR STR IR DR"
chr_list="chrX chrY chr1 chr2 chr3 chr4 chr5 chr6 chr7 chr8 chr9 chr10 chr11 chr12 chr13 chr14 chr15 chr16 chr17 chr18 chr19 chr20 chr21 chr22"

for CHR in ${chr_list}
do
  for NON_B in ${nb_list}
  do
    file=${CHR}_${NON_B}.bed
    bedtools merge -i ${file} > "${file/.bed/_merged.bed}"
  done
done

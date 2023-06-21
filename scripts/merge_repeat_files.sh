#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Incorrect number of parameters"
    echo "Specify the repeats folder"
    exit
fi

RepeatsFolder=$1

echo "RepeatsFolder: <$RepeatsFolder>"

cd $RepeatsFolder

for folder in "Bonobo" "Chimpanzee" "Human" "Gorilla" "B_Orangutan" "S_Orangutan" "Siamang"
do
  cd $folder;
  for file in $(ls *.bed); do bedtools merge -i $file > "${file/.bed/_merged.bed}"; done
  cd -;
done

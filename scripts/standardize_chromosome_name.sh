#!/bin/bash

for species in "B_Orangutan" "Gorilla" "Siamang" "Bonobo" "Human" "Chimpanzee" "S_Orangutan"
do
  python3 ./scripts/standardize_chromosome_name.py -i ./repeats/${species}/merged
done

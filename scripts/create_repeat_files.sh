#!/bin/bash

python3 scripts/create_repeat_files.py -s B_Orangutan -f ./repeats/Bornean_FinalAnnotations_June2023_v2.sort.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Bonobo -f ./repeats/Bonobo_FinalAnnotations_June2023_v2.sort.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Chimpanzee -f ./repeats/Chimpanzee_FinalAnnotations_June2023_v2.sort.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Gorilla -f ./repeats/Gorilla_FinalAnnotations_June2023_v2.sort.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Human -f ./repeats/CHM13v2.0_XY_FinalAnnotations_June2023_v2.sort.out -o ./repeats/
python3 scripts/create_repeat_files.py -s S_Orangutan -f ./repeats/Sumatran_FinalAnnotations_June2023_v2.sort.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Siamang -f ./repeats/Siamang_FinalAnnotations_June2023_v2.sort.out -o ./repeats/


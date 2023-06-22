#!/bin/bash

python3 scripts/create_repeat_files.py -s B_Orangutan -f ./repeats/input/Bornean_FinalAnnotations_June2023_v2.sort.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Bonobo -f ./repeats/input/Bonobo_FinalAnnotations_June2023_v2.sort.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Chimpanzee -f ./repeats/input/Chimpanzee_FinalAnnotations_June2023_v2.sort.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Gorilla -f ./repeats/input/Gorilla_FinalAnnotations_June2023_v2.sort.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Human -f ./repeats/input/CHM13v2.0_XY_FinalAnnotations_June2023_v2.sort.out -o ./repeats/
python3 scripts/create_repeat_files.py -s S_Orangutan -f ./repeats/input/Sumatran_FinalAnnotations_June2023_v2.sort.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Siamang -f ./repeats/input/Siamang_FinalAnnotations_June2023_v2.sort.out -o ./repeats/


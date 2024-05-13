#!/bin/bash

python3 scripts/create_repeat_files.py -s B_Orangutan -f ./repeats/input/Bornean.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Bonobo -f ./repeats/input/Bonobo.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Chimpanzee -f ./repeats/input/Chimpanzee.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Gorilla -f ./repeats/input/Gorilla.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Human -f ./repeats/input/CHM13v2.0_XY.out -o ./repeats/
python3 scripts/create_repeat_files.py -s S_Orangutan -f ./repeats/input/Sumatran.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Siamang -f ./repeats/input/Siamang.out -o ./repeats/

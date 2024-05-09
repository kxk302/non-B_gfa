#!/bin/bash

python3 scripts/create_repeat_files.py -s B_Orangutan -f ./repeats/input/mPonPyg2.pri.cur.20231122.combo.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Bonobo -f ./repeats/input/mPanPan1.pri.cur.20231122.combo2.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Chimpanzee -f ./repeats/input/mPanTro3.pri.cur.20231122.combo.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Gorilla -f ./repeats/input/mGorGor1.pri.cur.20231122.combo_final.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Human -f ./repeats/input/GCA_009914755.4_T2T-CHM13v2.0_genomic.fna.out -o ./repeats/
python3 scripts/create_repeat_files.py -s S_Orangutan -f ./repeats/input/mPonAbe1.pri.cur.20231205.combo.out -o ./repeats/
python3 scripts/create_repeat_files.py -s Siamang -f ./repeats/input/mSymSyn1.pri.cur.20231205.combo.out -o ./repeats/

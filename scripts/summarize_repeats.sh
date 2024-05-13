#!/bin/bash

python3 ./scripts/summarize_repeats.py -s B_Orangutan -f ./repeats/ -o ./repeats/summary_output/B_Orangutan_repeats_summary.tsv -n ./v2/output/Pongo_pygmaeus;
python3 ./scripts/summarize_repeats.py -s Bonobo -f ./repeats/ -o ./repeats/summary_output/Bonobo_repeats_summary.tsv -n ./v2/output/Pan_paniscus;
python3 ./scripts/summarize_repeats.py -s Chimpanzee -f ./repeats/ -o ./repeats/summary_output/Chimpanzee_repeats_summary.tsv -n ./v2/output/Pan_troglodytes;
python3 ./scripts/summarize_repeats.py -s Gorilla -f ./repeats/ -o ./repeats/summary_output/Gorilla_repeats_summary.tsv -n ./v2/output/Gorilla_gorilla;
python3 ./scripts/summarize_repeats.py -s Human -f ./repeats/ -o ./repeats/summary_output/Human_repeats_summary.tsv -n ./v2/output/Homo_sapiens;
python3 ./scripts/summarize_repeats.py -s S_Orangutan -f ./repeats/ -o ./repeats/summary_output/S_Orangutan_repeats_summary.tsv -n ./v2/output/Pongo_abelii;
python3 ./scripts/summarize_repeats.py -s Siamang -f ./repeats/ -o ./repeats/summary_output/Siamang_repeats_summary.tsv -n ./v2/output/Symphalangus_syndactylus;

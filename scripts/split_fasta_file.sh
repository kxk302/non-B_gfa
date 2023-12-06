#!/bin/bash

input_dir=${1:-"."}

python3 ./scripts/split_fasta_file.py -f ${input_dir}/input/aggregate_fasta_files/mGorGor1.pri.cur.20231122.fasta -o ${input_dir}/input/Gorilla_gorilla/seqs_srcdir -p chr

python3 ./scripts/split_fasta_file.py -f ${input_dir}/input/aggregate_fasta_files/mPanPan1.pri.cur.20231122.fasta -o ${input_dir}/input/Pan_paniscus/seqs_srcdir -p chr

python3 ./scripts/split_fasta_file.py -f ${input_dir}/input/aggregate_fasta_files/mPanTro3.pri.cur.20231122.fasta -o ${input_dir}/input/Pan_troglodytes/seqs_srcdir -p chr

python3 ./scripts/split_fasta_file.py -f ${input_dir}/input/aggregate_fasta_files/mPonAbe1.pri.cur.20231122.fasta -o ${input_dir}/input/Pongo_abelii/seqs_srcdir -p chr

python3 ./scripts/split_fasta_file.py -f ${input_dir}/input/aggregate_fasta_files/mPonPyg2.pri.cur.20231122.fasta -o ${input_dir}/input/Pongo_pygmaeus/seqs_srcdir -p chr

python3 ./scripts/split_fasta_file.py -f ${input_dir}/input/aggregate_fasta_files/mSymSyn1.pri.cur.20231122.fasta -o ${input_dir}/input/Symphalangus_syndactylus/seqs_srcdir -p chr

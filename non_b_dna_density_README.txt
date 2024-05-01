1. Activate the Python virtual environment via the following command:

   . ./venv/bin/activate

2. For each species, calculate the chromosome sequence length by running the following script:

   ./scripts/get_chr_length.sh

   This script calls ./scripts/get_chr_length.py for each species and each chromosome, and creates genome txt files for
   each chromosome (chr1.txt, chr2.txt,..., chrY.txt) to be used by bedtools makewindows later.

3. For each species, create windows of specific size (say, 100kb) by running the following script:

   ./scripts/make_windows.sh ./output/ 100000

   The script calls 'bedtools makewindows' command. You must pass two parameters to the script:
     1) Path to nBMST output, and
     2) Window size

   The nBMST output folder is assumed to have the following subfolders: Gorilla_gorilla, Pan_paniscus, 
   Pongo_abelii, Symphalangus_syndactylus, Homo_sapiens, Pan_troglodytes, Pongo_pygmaeus

4. Backup nBMST inverted/direct/mirrored repeats, before we filter them based on spacer length, by running the following script:

   ./scripts/backup_repeats.sh ./output/

   You must pass the path to nBMST output to the script as parameter.

5. For each species, filter the inverted/direct/mirrored repeats based on spacer length, by running the script:

   ./scripts/filter.sh ./output/ 15

   You must pass the path to nBMST output and spacer length filter value to the script as parameters.

6. For each species, and each chromosome, aggregate the non-B DNA files into one .bed file, by running the following script:

   ./scripts/concat_non_b_dna_files.sh ./output/

   This script calls ./scripts/concat_non_b_dna_files.py for each species and chromosome, and for each non-B DNA type AND all of
   the non-b DNA types combined.

7. For each species, create a non-B DNA density file, by running the following command:

   ./scripts/create_density_files.sh ./output/

   This script calls 'bedtools coverage', for each species and chromosome, and for each non-B DNA type AND all of
   the non-b DNA types combined, to create intermediate density files, then aggregates them by calling
   ./scripts/create_density_files.py.

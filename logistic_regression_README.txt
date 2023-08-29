Simple Logistic Regression

1. Suppoe non-B_gfa is cloned into <MyWorkspace> directory. Create the following input directory structure in
   <MyWorkspace>/non-B_gfa directory. For each species, copy the chrX and chrY new onto old mapping data files
   to the appropriate seqs_srcdir folder.

input/
├── Gorilla_gorilla
│   ├── Re_aligning_old_to_new_assemblies
│   │   ├── gorGor.chrX.new_onto_old.winnowmap.covered.dat
│   │   └── gorGor.chrY.new_onto_old.winnowmap.covered.dat
├── Homo_sapiens
│   ├── Re_aligning_old_to_new_assemblies
│   │   ├── chm13.chrX.density.bed
│   │   └── hg002.chrY.density.bed
├── Pan_paniscus
│   ├── Re_aligning_old_to_new_assemblies
│   │   ├── panPan.chrX.new_onto_old.winnowmap.covered.dat
│   │   └── panPan.chrY.new_onto_old.winnowmap.covered.dat
├── Pan_troglodytes
│   ├── Re_aligning_old_to_new_assemblies
│   │   ├── panTro.chrX.new_onto_old.winnowmap.covered.dat
│   │   └── panTro.chrY.new_onto_old.winnowmap.covered.dat
├── Pongo_abelii
│   ├── Re_aligning_old_to_new_assemblies
│   │   ├── ponAbe.chrX.new_onto_old.winnowmap.covered.dat
│   │   └── ponAbe.chrY.new_onto_old.winnowmap.covered.dat

2. Create the input file for Simple Logistic Regression (SLR), for all species (except for Pongo_pygmaeus and
   Symphalangus_syndactylus), and for all non-B DNA types, by running the following script.

   ./scripts/logistic_regression_input.sh

   This script calls ./scripts/logistic_regression_input.py for each species + non-B DNA combination (including 'all').
   You pass a window size and novelty threshold as input parametyers to logistic_regression_input.py. The script reads
   the pre-existing and non-b DNA density files, and creates a novel_label column, where the value of the column is True
   if the novelty of the window exceeds the threshold, and writes the non_b_dna_count and novel_label to the output file.

3. For all species (except for Pongo_pygmaeus and Symphalangus_syndactylus), and all non-B DNA types, run Simple Logistic
   Regression and save the model summary to file by running the following script:

   ./scripts/logistic_regression.sh

   This script calls ./scripts/logistic_regression.R for each species and non-B DNA combination (including 'all').

Multiple Logistic Regression

1. Create the input file for Multiple Logistic Regression (rMSLR), for all species (except for Pongo_pygmaeus and
   Symphalangus_syndactylus), by running the following script.
 
   ./scripts/multiple_logistic_regression_input.sh

   This script calls ./scripts/multiple_logistic_regression_input.py for each species. You pass a window size and novelty
   threshold as input parametyers to multiple_logistic_regression_input.py. The script reads the pre-existing density files,
   reads all non-b DNA density files (for chrX and chrY) and concatenates them column wise. It then creates a novel_label
   column, where the value of the column is True if the novelty of the window exceeds the threshold, and writes the
   non_b_dna_count and for all non-b DNA types and novel_label to the output file.

2. For all species (except for Pongo_pygmaeus and Symphalangus_syndactylus), and all non-B DNA types, run Multiple Logistic
   Regression and save the model summary to file by running the following script:

   ./scripts/multiple_logistic_regression.sh

   This script calls ./scripts/multiple_logistic_regression.R for each species.

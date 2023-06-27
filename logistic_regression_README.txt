Simple Logistic Regression

1. Create the input file for Simple Logistic Regression (SLR), for all species (except for Pongo_pygmaeus and
   Symphalangus_syndactylus), and for all non-B DNA types, by running the following script.
 
   ./scripts/logistic_regression_input.sh

   This script calls ./scripts/logistic_regression_input.py for each species + non-B DNA combination (including 'all').
   You pass a window size and novelty threshold as input parametyers to logistic_regression_input.py. The script reads
   the pre-existing and non-b DNA density files, and creates a novel_label column, where the value of the column is True
   if the novelty of the window exceeds the threshold, and writes the non_b_dna_count and novel_label to the output file.

2. For all species (except for Pongo_pygmaeus and Symphalangus_syndactylus), and all non-B DNA types, run Simple Logistic
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

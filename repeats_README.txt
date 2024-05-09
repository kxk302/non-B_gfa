1. The RepeatMasker files we got from Gabby Hartley (from Rachel O'Neill's group at UConn) are in this directory:

   /nfs/brubeck.bx.psu.edu/scratch6/makova_lab/downloads/primate_T2T/assemblies/annotations/repeatannotations_final/

2. There are 8 files for Bonobo, Gorilla, Bornean Orangutan, Sumataran Orangutan, Chimpanzee, Siamang, CHM13 and HG002.

3. Run ./scripts/create_repeat_files.sh (Calls 'create_repeat_files.py' for each species) to create repeat files (for
   61 repeat type listed in create_repeat_files.py), for chr1 to chr24, chrX and chrY, for each species listed in step 2.
   We used CHM13 for Human. This scripts uses the RepeatMasker files as input, and generates repeat files in ./repeats/<species>
   folder. For 5 "Satellite*" and "Unspecified" repeat types, the script creates a file for each sub-type. The list of sub-types
   for each 5 "Satellite*" and "Unspecified" repeat types can be found in REPEAT_SUBLABELS variable in
   ./scripts/create_repeat_files.py. There are a total of 27 sub-types for "Satellite*" and "Unspecified" repeat types, hence,
   27*26=702 files for chromosomes 1 to 24, and X and Y are created. For the remaining 55 repeat types, 55*26=1430 files are
   created for chromosomes 1 to 24 and X and Y. Hence, the number of files created for each species is  1430 + 702 = 2132.

4. Run ./scripts/merge_repeat_files.sh (Calls 'bedtools merge' for each species' repeat files) to combine overlapping
   intervals, to avoid double counting them. The output file will have '_merged' added to their name, right before the
   file extesion. For example, for repeat file 'chrX_Satellite.bed', the script outputs 'chrX_Satellite_merged.bed'.

5. Run ./scripts/merge_non_b_files.sh (Calls 'bedtools merge' for each species' nBMST output files) to combine overlapping
   intervals, to avoid double counting them. The output file will have '_merged' added to their name, right before the
   file extesion. For example, for non_b file 'chrX_APR.bed', the script outputs 'chrX_APR_merged.bed'.

   NOTE: Now that you have merged non-B DNA output files, you can also create a summary table that for each species provides
   the total length and normalized total length of each non-B DNA type (normalized by chromosome length). The summary tables
   are created in ./summary_output folder by running ./scripts/summarize_nBMST.sh (which call ./scripts/summarize_nBMST.py).

6. Run ./scripts/intersect_repeat_files.sh (Calls 'intersect_repeat_file.sh' for each species). For each species,
   intersect_repeat_file.sh calls 'bedtools intersect' to find the overlaps between a repeat file and each of non-B
   DNA annotations APR, DR, GQ, IR, MR, STR, and Z. We have 2132 repeat files for each species, and since there are 7
   non-B DNA types, intersect_repeat_files.sh creates 14924 intersect files.

7. Run ./scripts/summarize_repeats.sh (Calls 'summarize_repeats.py' for each species). For each species, and for each repeat
   type, sum up the length of intervals specified in the merged repeat files from step 4; For each species, this generates a
   list composed of 82 numbers. For each species, for each repeat type, and for each non-B DNA type, sum up the length of
   intervals specified in the intersect files from step 6; For each species, this generates a table compsed of 82 rows (repeat
   types) and 7 columns (non-b DNA types). Divide the values in each row of this table (say, row 1 represents 'Satellite'
   repeat type) by the corresponding value in the list (say, element 1 of the list represents 'Satellite' repeat). This
   normalizes the value to be between 0 and 1. Finally, we divided table cells by their corresponding non-B DNA density.
   This allows us to detect enrichment, i.e. cases where density in a certain cell is higher than the non-B DNA density.
   The normalized table is saved to a .tsv file in ./repeats/summary_output folder.

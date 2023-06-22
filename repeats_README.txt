1. The RepeatMasker files we got from Gabby Hartley (from Rachel O'Neill's group at UConn) are in this directory:

   /nfs/brubeck.bx.psu.edu/scratch6/makova_lab/downloads/primate_T2T/assemblies/annotations/repeatannotations_final/
  
2. There are 8 files for Bonobo, Gorilla, Bornean Orangutan, Sumataran Orangutan, Chimpanzee, Siamang, CHM13 and HG002.

3. Run ./scripts/create_repeat_files.sh (Calls 'create_repeat_files.py' for each species) to create repeat files (for 
   each repeat type listed below), for chrX and chrY, for each species listed in step 2. We used CHM13 for Human. This 
   scripts uses the RepeatMasker files as input, and generates repeat files in ./repeats/<species> folder. For each of 
   the species, 12 repeat files are generated (6 repeat types and 2 chromosomes). 

   Satellite
   Satellite/acro
   Satellite/centr
   Satellite/subtelo
   Satellite/Y-chromosome
   Simple_repeat

4. Run ./scripts/merge_repeat_files.sh (Calls 'bedtools merge' for each species' repeat files) to combine overlapping 
   intervals, to avoid double counting them. The output file will have '_merged' added to their name, right before the 
   file extesion. For example, for repeat file 'chrX_Satellite.bed' to scripts outputs 'chrX_Satellite_merged.bed'.

5. Run ./scripts/intersect_repeat_files.sh (Calls 'intersect_repeat_file.sh' for each species). For each species, 
   intersect_repeat_file.sh calls 'bedtools intersect' to find the overlaps between a repeat file and each of non-B 
   DNA annotations APR, DR, GQ, IR, MR, STR, and Z. We have 12 repeat files for each species, and since there are 7 non-B DNA 
   types, intersect_repeat_files.sh creates 84 intersect files.  

6. Run ./scripts/summarize_repeats.sh (Calls 'summarize_repeats.py' for each species). For each species, and for each repeat 
   type, sum up the length of intervals specified in the merged repeat files from step 4; For each species, this generates a 
   list composed of 6 numbers. For each species, for each repeat type, and for each non-B DNA type, sum up the length of 
   intervals specified in the intersect files from step 5; For each species, this generates a table compsed of 6 rows (repeat 
   types) and 7 columns (non-b DNA types). Divide the values in each row of this table (say, row 1 represents 'Satellite' 
   repeat type) by the corresponding value in the list (say, element 1 of the list represents 'Satellite' repeat). This 
   normalizes the value to be between 0 and 1. The normalized table is saved to a .tsv file in ./repeats/summary_output 
   folder, as well as a heatmap generated off the normalized table.

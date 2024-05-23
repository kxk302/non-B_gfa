1. Clone the non-B_gfa repository by running the following command in <MyWorkspace> directory:

   https://github.com/kxk302/non-B_gfa.git

   This creates a non-B_gfa folder in <MyWorkspace> directory

2. Create the following directory structure in <MyWorkspace> directory.

input/
├── Gorilla_gorilla
│   └── seqs_srcdir
├── Pan_paniscus
│   └── seqs_srcdir
├── Pan_troglodytes
│   └── seqs_srcdir
├── Pongo_abelii
│   └── seqs_srcdir
├── Pongo_pygmaeus
│   └── seqs_srcdir
├── Symphalangus_syndactylus
│   └── seqs_srcdir
└── aggregate_fasta_files

3. Copy the aggregate fasta files from brubeck to '<MyWorkspace>/input/aggregate_fasta_files' directory.
   Aggregate fasta files are in '/nfs/brubeck.bx.psu.edu/scratch4/makova_lab/downloads/primate_T2T/assemblies/v2'
   folder on brubeck. After copying the files, the contents of the directory should be as below:

input/aggregate_fasta_files/
├── README
├── chm13v2.0.fa
├── mGorGor1.pri.cur.20231122.fasta
├── mPanPan1.pri.cur.20231122.fasta
├── mPanTro3.pri.cur.20231122.fasta
├── mPonAbe1.pri.cur.20231205.fasta
├── mPonPyg2.pri.cur.20231122.fasta
└── mSymSyn1.pri.cur.20240514.fasta

4. For each aggregate fasta file in 'input/aggregate_fasta_files/' folder, run the following command to split the
   aggregate fasta files into individual fasta files, so we have one fasta file for each chromosome.

   ./scripts/split_fasta_files.sh <AggregateFastaFileName>

   After the script runs to completion, move the individual fasta files to the appropriate folder. E.g., if you split
   'mGorGor1.pri.cur.20231122.fasta', move the individual fasta files to './input/Gorilla_gorilla/seqs_srcdir'.

5. Delete the following redundant files:

   input/Homo_sapiens/seqs_srcdir/chrM.fa
   input/Pan_Paniscus/seqs_srcdir/chr1522_pat_hsa1421_random_utig4-145.fasta
   input/Pan_Paniscus/seqs_srcdir/chr1522_pat_hsa1421_random_utig4-147.fasta
   input/Pan_Paniscus/seqs_srcdir/chr1522_pat_hsa1421_random_utig4-325.fasta
   input/Pan_Paniscus/seqs_srcdir/chr1522_pat_hsa1421_random_utig4-839.fasta
   input/Pan_Paniscus/seqs_srcdir/chr1522_pat_hsa1421_random_utig4-95.fasta
   input/Pongo_abelii/seqs_srcdir/chr18_hap1_hsa16_random_utig4-1074.fasta
   input/Pongo_abelii/seqs_srcdir/chr18_hap1_hsa16_random_utig4-1076.fasta
   input/Pongo_abelii/seqs_srcdir/chr18_hap1_hsa16_random_utig4-3743.fasta
   input/Pongo_abelii/seqs_srcdir/chr18_hap1_hsa16_random_utig4-3745.fasta

6. Standardize the name of each individual fasta file, (e.g., rename 'chr1_pat_hsa1.fasta' into 'chr1.fa') by running
   the following script in every ./input/<species>/seq_srcdir

   for file in $(ls *.fasta);do mv ${file} ${file/_*.fasta/.fa};done

   After running './scripts/split_fasta_files.sh' for all aggregate fasta files, moving the individual fasta files to the
   appropriate 'seqs_srcdir' folder, and standardizing individual fasta file names, the contents of the input directory
   should be as below:

input/
├── Gorilla_gorilla
│   └── seqs_srcdir
│       ├── chr1.fa
│       ├── chr2.fa
│       ├── .......
│       ├── chrX.fa
│       └── chrY.fa
├── Homo_sapiens
│   └── seqs_srcdir
│       ├── chr1.fa
│       ├── chr2.fa
│       ├── .......
│       ├── chrX.fa
│       └── chrY.fa
├── Pan_paniscus
│   └── seqs_srcdir
│       ├── chr1.fa
│       ├── chr2.fa
│       ├── .......
│       ├── chrX.fa
│       └── chrY.fa
├── Pan_troglodytes
│   └── seqs_srcdir
│       ├── chr1.fa
│       ├── chr2.fa
│       ├── .......
│       ├── chrX.fa
│       └── chrY.fa
├── Pongo_abelii
│   └── seqs_srcdir
│       ├── chr1.fa
│       ├── chr2.fa
│       ├── .......
│       ├── chrX.fa
│       └── chrY.fa
├── Pongo_pygmaeus
│   └── seqs_srcdir
│       ├── chr1.fa
│       ├── chr2.fa
│       ├── .......
│       ├── chrX.fa
│       └── chrY.fa
└── Symphalangus_syndactylus
    └── seqs_srcdir
│       ├── chr1.fa
│       ├── chr2.fa
│       ├── .......
│       ├── chrX.fa
│       └── chrY.fa

7. Standardize the chromosome name in .fa files by running the following script in
   every ./input/<species>/seq_srcdir:

   for file in $(ls *.fa); do sed -i '' 's/_.*//' $file;done

   This script, for example, changes '>chr1_pat_hsa1' to '>chr1' in 'Gorilla_gorilla/seqs_srcdir/chr1.fa'.
   We need standardized chromosome names for './scripts/get_chr_length.sh' to work properly.

8. Create the following output directory structure in <MyWorkspace>/non-B_gfa directory.

output/
├── Gorilla_gorilla
├── Homo_sapiens
├── Pan_paniscus
├── Pan_troglodytes
├── Pongo_abelii
├── Pongo_pygmaeus
└── Symphalangus_syndactylus

9. Run ./scripts/run_nBMSTs.sh. This script calls ./scripts/run_nBMST.sh for each species and each chromosome.
   For each species, the output files are copied to the appropriate output folder.

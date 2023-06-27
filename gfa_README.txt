1. Clone the non-B_gfa repository by running the following command in <MyWorkspace> directory:

   https://github.com/kxk302/non-B_gfa.git

   This creates a non-B_gfa folder in <MyWorkspace> directory

2. Create the following input directory structure in <MyWorkspace>/non-B_gfa directory. For each species,
   copy the chrX and chrY fasta files (named chrX.fa and chrY.fa) to the appropriate seqs_srcdir folder.

input/
├── Gorilla_gorilla
│   └── seqs_srcdir
│       ├── chrX.fa
│       └── chrY.fa
├── Homo_sapiens
│   └── seqs_srcdir
│       ├── chrX.fa
│       └── chrY.fa
├── Pan_paniscus
│   └── seqs_srcdir
│       ├── chrX.fa
│       └── chrY.fa
├── Pan_troglodytes
│   └── seqs_srcdir
│       ├── chrX.fa
│       └── chrY.fa
├── Pongo_abelii
│   └── seqs_srcdir
│       ├── chrX.fa
│       └── chrY.fa
├── Pongo_pygmaeus
│   └── seqs_srcdir
│       ├── chrX.fa
│       └── chrY.fa
└── Symphalangus_syndactylus
    └── seqs_srcdir
        ├── chrX.fa
        └── chrY.fa

3. Create the following output directory structure in <MyWorkspace>/non-B_gfa directory.

output/
├── Gorilla_gorilla
├── Homo_sapiens
├── Pan_paniscus
├── Pan_troglodytes
├── Pongo_abelii
├── Pongo_pygmaeus
└── Symphalangus_syndactylus

4. Run ./scripts/run_nBMST.sh. This script calls ./scripts/run_nBMST.sh for each species and for chrX and chrY. The output files 
   are moved from <MyWorkspace>/non-B_gfa directory to the output folder.

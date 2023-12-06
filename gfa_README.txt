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
├── mGorGor1.pri.cur.20231122.fasta
├── mPanPan1.pri.cur.20231122.fasta
├── mPanTro3.pri.cur.20231122.fasta
├── mPonAbe1.pri.cur.20231122.fasta
├── mPonPyg2.pri.cur.20231122.fasta
└── mSymSyn1.pri.cur.20231122.fasta

4. Run the following command to split the aggregate fasta files, so we have 1 fasta file for each chromosome.

   ./scripts/split_fasta_file.sh .

   This script takes one input parameter: the 'input' folder's parent directory (which is '.', or current
   folder, in this case ). This script calls './scripts/split_fasta_file.py' for each species, and places
   the split fasta files in the appropriate folder. After running the script, the contents of the directory
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

5. Create the following output directory structure in <MyWorkspace>/non-B_gfa directory.

output/
├── Gorilla_gorilla
├── Homo_sapiens
├── Pan_paniscus
├── Pan_troglodytes
├── Pongo_abelii
├── Pongo_pygmaeus
└── Symphalangus_syndactylus

6. Run ./scripts/run_nBMSTs.sh. This script calls ./scripts/run_nBMST.sh for each species and each chromosome.
   For each species, the output files are copied to the appropriate output folder.

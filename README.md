# Split Fasta

Split Fasta is a command-line tool which allows you to split the Fasta file with multiple sequences into individual Fasta files.

## Installation

You can install Split Fasta from [PyPI](https://pypi.org/project/split-fasta/):
```pip install split-fasta```

The Split Fasta works with Python 3.6 & above.

## How to use?

The Split Fasta is a command-line tool, named splitfasta. To start it you have to go to the folder containing the Fasta file and then use the following syntax:-
```splitfasta filename.fasta```

And it will split the combined Fasta file into individual files and save it into filename_split_files directory with names from filename_1 to filename_n.

It accepts only .fasta and .fa files where each sequence is separated by '>'

The example input file is :-
```
>ID-1
ATGGCTCGAGCACCCGAGGAAGTCGAAGGCGGAGCCCAAGAAGAAGCTCCACCCCTCGCACGAGGCGGTGTTCGAACGCT
>ID-2
ATGGCTCGAGCACCCGAGGAAGTCGAAGGCGGAGCCCAAGAAGAAGCTCCACCCCTCGCACGAGGCGGTGTTCGAACGCT
```

## Detailed Tutorial

You can check out the detailed tutorial [here](https://saralgyaan.com/posts/split-fasta-file-with-multiple-sequences-into-individual-fasta-files/)

## License

© 2020 Udit Vashisht

This repository is licensed under the MIT license. See LICENSE for details.

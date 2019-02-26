# Challenges
Coding challenges in Python

## Maximum squares challenge:
Here the aim of the challenge is to find a square of ones in a random binary matrix. For example:

0 0 0 0 1 1 

1 1 1 0 0 0

1 1 1 0 1 1

1 1 1 0 0 1

0 0 1 1 0 0

The output here should be 9

## Consensus challenge:
Given a matrix of DNA sequences, take a consensus strand and calculate the consensus matrix for each nucleotide
GCAACT

EXAMPLE:
for the the input file below the output is as follows:

### input
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT


### output
DNA strings:
ATCCAGCT
GGGCAACT
ATGGATCT
AAGCAACC
TTGGAACT
ATGCCATT
ATGGCACT
A       5 1 0 0 5 5 0 0
C       0 0 1 4 2 0 6 1
G       1 1 6 3 0 1 0 0
T       1 5 0 0 0 1 1 6
The following consenus strand has been found: ATGCAACT



## Challenge strairs:
There is a stairs with 100 steps. It is possible to have different routes to the top of the stairs. For example skipping each step. The question is: In how many ways can you climb the stairs given that it is only alowwed to take either one stairs or skip a stairs? 

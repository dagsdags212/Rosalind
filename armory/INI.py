"""
PROBLEM:

This initial problem is aimed at familiarizing you with Rosalind's task-solving pipeline. To solve it, you merely have 
to take a given DNA sequence and find its nucleotide counts; this problem is equivalent to “Counting DNA Nucleotides” 
in the Stronghold.

Of the many tools for DNA sequence analysis, one of the most popular is the Sequence Manipulation Suite. Commonly known 
as SMS 2, it comprises a collection of programs for generating, formatting, and analyzing short strands of DNA and polypeptides.

One of the simplest SMS 2 programs, called `DNA stats`, counts the number of occurrences of each nucleotide in a given 
strand of DNA. An online interface for DNA stats can be found here.

GIVEN:

A DNA string s of length at most 1000 bp.


RETURN:

Four integers (separated by spaces) representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' 
occur in s. Note: You must provide your answer in the format shown in the sample output below.
"""

def count_nucleotides(dna_seq: str) -> list[int]:
    """
    Counts the number of nucleotides in a given DNA sequence. The base counts are given in the following order:
    "A", "C", "G", "T"

    PARAMETERS
    ==========
    > dna_seq (str): a DNA sequence

    RETURN
    ======
    A list of unique nucleotide counts
    """
    dna_seq = dna_seq.upper()
    counts = {base: 0 for base in "ACGT"}
    for base in dna_seq:
        if base not in "ACGT":
            raise ValueError("DNA sequence must only contain 'A', 'C', 'G', or 'T'")
        counts[base] += 1
    return list(counts.values())

def main() -> None:
    from sys import argv
    dna_seq = argv[1].strip()
    counts = count_nucleotides(dna_seq)
    print(*counts)

if __name__ == "__main__":
    main()

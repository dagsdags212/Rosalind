"""
PROBLEM:

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string `t` corresponding to a coding strand, its transcribed RNA string u is formed 
by replacing all occurrences of 'T' in t with 'U' in u.

GIVEN:

A DNA string `t` having length at most 1000 nt.

RETURN:

The transcribed RNA string of `t`.
"""

def translate(dna_seq: str) -> str:
    """
    Returns a translated mRNA from a DNA sequence.

    PARAMETERS
    ==========
    > dna_seq (str): A DNA sequence containing 'A', 'C', 'G', or 'T'

    return
    ======
    A translated RNA string
    """
    dna_seq = dna_seq.upper()
    rna_seq = dna_seq.replace('T', 'U')
    return rna_seq

def main() -> None:
    from sys import argv
    dna_seq = argv[1].strip()
    rna_seq = translate(dna_seq)
    print(rna_seq)

if __name__ == '__main__':
    main()

"""
PROBLEM:

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string `s` is the string $s^{c}$ formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

GIVEN:

A DNA string `s` of length at most 1000 bp.

RETURN:

The reverse complement $s^{c}$ of `s`.

"""

def reverse_complement(dna_seq: str) -> str:
    """
    Returns the reverse complement of a DNA sequence.

    PARAMETERS
    ==========
    > dna_seq (str): A DNA sequence containing 'A', 'C', 'G', or 'T'

    RETURN
    ======
    The reverse complement of the given sequence  
    """
    DNA2DNA = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # initialize reverse complement as an empty string
    rc = ''
    dna_seq = dna_seq.upper()
    # add each complementary base to the start of `rc`
    for base in dna_seq:
        rc = DNA2DNA[base] + rc
    return rc

def main() -> None:
    from sys import argv
    dna_seq = argv[1].strip()    
    rc = reverse_complement(dna_seq)
    print(rc)

if __name__ == '__main__':
    main()

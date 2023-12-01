"""
PROBLEM:

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

GIVEN:

A DNA string s of length at most 1000 nt.

RETURN:

Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
  
"""

def count_unique_nucleotides(dna_seq: str) -> dict[str, int]:
    """Returns the count of each unique nucleotide in a given DNA string.
    
    PARAMETERS
    ==========
    > dna_seq (str): A DNA string using the alphabet 'ACGT'

    RETURN
    ======
    A dictionary mapping each unique nucleotide to its count in the DNA sequence.
    """
    DNA_ALPHABET = 'ACGT'
    # initialize each nucleotide with a count of zero
    nuc_count = {base: 0 for base in DNA_ALPHABET}
    # convert each character into uppercase
    dna_seq = dna_seq.upper()
    for base in dna_seq:
        # raise error if the base if invalid
        if base not in DNA_ALPHABET:
            raise ValueError('DNA sequence can only contain `A`, `C`, `G`, or `T`')
        nuc_count[base] += 1
    return nuc_count

def main() -> None:
    from sys import argv
    dna_seq = argv[1].strip()
    nuc_count = count_unique_nucleotides(dna_seq)
    counts = list(nuc_count.values())
    print(*counts)

if __name__ == "__main__":
    main()

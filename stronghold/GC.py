"""
PROBLEM:

The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'.
For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string
has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string 
labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>',
followed by some labeling information. Subsequent lines contain the string itself; 
the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where 
"xxxx" denotes a four-digit code between 0000 and 9999.

GIVEN:

At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

RETURN:

The ID of the string having the highest GC-content, followed by the GC-content of that string. 
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated.

"""

def compute_gc(dna_seq: str) -> float:
    """
    Computes for the total GC content of a DNA sequence.

    PARAMETERS
    ==========
    > dna_seq (str): a DNA sequence

    RETURN
    ======
    A float denoting the GC content of the given DNA sequence
    """
    dna_seq = dna_seq.upper()
    # initialize count to zero
    gc_count = 0
    for base in dna_seq:
        if base in 'GC':
            gc_count += 1
    gc_content = gc_count / len(dna_seq) * 100
    return round(gc_content, 6)

def parse_fasta(fasta_file: str) -> dict[str, float]:
    """
    Returns a mapping between sequence IDs and GC content.

    PARAMETERS
    ==========
    > fasta_file (str): a sequence of strings in FASTA format

    RETURN
    ======
    A dictionary with sequence IDs as keys and GC content as values
    """
    seqs = {}
    with open(fasta_file, "r") as fhandle:
        curr_id = None
        for line in fhandle.readlines():
            line = line.strip()           
            if line[0] =='>':
                curr_id = line[1::]
                seqs[curr_id] = ""
            else:
                seqs[curr_id] += line   
    # replace sequences with their respective GC content
    for id, seq in seqs.items():
        seqs[id] = compute_gc(seq)
    return seqs

def main() -> None:
    from sys import argv
    fasta_path = argv[1]
    seqs = parse_fasta(fasta_path)   
    max_id, max_gc = None, 0
    for seq_id, gc in seqs.items():
        if gc > max_gc:
            max_gc = gc
            max_id = seq_id 
    print(max_id)
    print(max_gc)

if __name__ == '__main__':
    main()    

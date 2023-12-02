"""
PROBLEM:

The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet 
(all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. 
Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

GIVEN:

An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

RETURN:

The protein string encoded by s.
"""

def translate(rna_seq: str) -> str:
    """
    Converts an RNA sequence into a polypeptide string.

    PARAMETERS
    ==========
    > rna_seq (str): an mRNA string

    RETURN
    ======
    A polypeptide string composed of amino acids
    """
    RNA_CODON_TABLE = {
        "AUG": "M",
        "UUU": "F", "UUC": "F",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y",
        "UGU": "C", "UGC": "C",
        "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H",
        "CAA": "Q", "CAG": "Q",
        "CGU": "R",  "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", 
        "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
        "UAA": "*", "UGA": "*", "UAG": "*",       
    }
    peptide = ""
    rna_seq = rna_seq.upper()
    for i in range(0, len(rna_seq), 3):
        codon = rna_seq[i:i+3]
        peptide += RNA_CODON_TABLE[codon]
    return peptide

def main() -> None:
    from sys import argv
    rna_seq = argv[1]
    peptide = translate(rna_seq)
    print(peptide)

if __name__ == "__main__":
    main()

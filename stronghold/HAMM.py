"""
PROBLEM:

Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), 
is the number of corresponding symbols that differ in s and t.

GIVEN:

Two DNA strings s and t of equal length (not exceeding 1 kbp).

RETURN:

The Hamming distance dH(s,t).
"""

def hamming_distance(reference_str: str, query_str: str) -> int:
    """
    Computes for the number of element-wise differences between two strings.

    PARAMETERS
    ==========
    > reference_str (str): the reference string to be matched
    > query_str (str): the query string that deviates

    RETURN
    ======
    An integer count of the number of mismatches between the reference and query strings
    """
    assert len(reference_str) == len(query_str), "Both input strings must be of the same length"
    mismatches = 0
    for i in range(len(reference_str)):
        if reference_str[i] != query_str[i]:
            mismatches += 1
    return mismatches 

def main() -> None:
    from sys import argv
    reference = argv[1].strip().upper()
    query = argv[2].strip().upper()
    num_mm = hamming_distance(reference, query)
    print(num_mm)

if __name__ == '__main__':
    main()

"""
PROBLEM:

Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s 
(as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its left, including itself 
(e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). 
The symbol at position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s;
for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if 
it occurs more than once as a substring of s.

GIVEN:

Two DNA strings s and t (each of length at most 1 kbp).

RETURN:

All locations of t as a substring of s.
"""

def find_matches(ref_seq: str, sub_seq: str) -> list[int]:
    """
    Returns a list of indices where `sub_seq` matches a region of `ref_seq`.

    PARAMETERS
    ==========
    > ref_seq (str): a sequence the serves as the reference string
    > sub_seq (str): a substring of ref_seq

    RETURN
    ======
    A list of indices where `sub_seq` fully matches within `ref_seq`
    """
    k = len(sub_seq)
    ref_seq, sub_seq = ref_seq.upper(), sub_seq.upper()
    matching_idx = []
    for i in range(len(ref_seq)-k):
        if ref_seq[i:i+k] == sub_seq:
            matching_idx.append(i+1)
    return matching_idx

def main() -> None:
    from sys import argv
    ref_seq, sub_seq = argv[1:3]   
    matches = find_matches(ref_seq, sub_seq)
    print(*matches)

if __name__ == "__main__":
    main()

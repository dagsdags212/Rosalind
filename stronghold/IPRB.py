"""
PROBLEM:

Probability is the mathematical study of randomly occurring phenomena. We will model such a
phenomenon with a random variable, which is simply a variable that can take a number of different 
distinct outcomes depending on the result of an underlying random process.

For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X represent 
the random variable corresponding to the color of a drawn ball, then the probability of each of 
the two outcomes is given by Pr(X=red)=35 and Pr(X=blue)=25.

Random variables can be combined to yield new random variables. Returning to the ball example, let Y
model the color of a second ball drawn from the bag (without replacing the first ball). The probability 
of Y being red depends on whether the first ball was red or blue. To represent all outcomes of X and Y, 
we therefore use a probability tree diagram. This branching diagram represents all possible individual 
probabilities for X and Y, with outcomes at the endpoints ("leaves") of the tree. The probability of any 
outcome is given by the product of probabilities along the path from the beginning of the tree; 
see Figure 2 for an illustrative example.

An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event 
can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, 
let A be the event "Y is blue." Pr(A) is equal to the sum of the probabilities of two different outcomes: 
Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 310+110=25 (see Figure 2 above).

GIVEN:

Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals 
are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

RETURN:

The probability that two randomly selected mating organisms will produce an individual possessing a 
dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate
"""

def prob_dominant(HH: int, Hh: int, hh: int) -> float:
    """
    Computes for the probability that the given population will produce at least one progeny with
    a dominant allele (H). It is assumed that each parent can mate with every other parent in the
    population.

    PARAMETERS
    ==========
    > HH (int): number of homozygous dominant parents
    > Hh (int): number of heterozygous parents
    > hh (int): number of homozygous recessive parents

    RETURNS
    =======
    A float probability that the given parent population will produce at least one progeny with a 
    dominant allele. 
    """
    total = HH+Hh+hh
    # compute for the probabilities of getting 2Hh, 2hh, or 1Hh+1hh
    p_two_rec = (hh/total) * ((hh-1)/(total-1))    
    p_two_het = (Hh/total) * ((Hh-1)/(total-1))
    p_het_rec = (Hh/total) * (hh/(total-1)) + (hh/total) * (Hh/(total-1))

    # compute the probability of getting at least one recessive
    p_rec = p_two_rec + p_two_het/4 + p_het_rec/2
    # get the inverse
    p_dom = 1 - p_rec
    return p_dom
    
def main() -> None:
    from sys import argv
    k, m, n = list(map(int, argv[1:4]))
    p_dom = prob_dominant(k, m, n)
    print(p_dom)

if __name__ == '__main__':
    main()

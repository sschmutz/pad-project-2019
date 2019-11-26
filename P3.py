"""This module creates a pairwise distance matrix from aligned sequences
using the JC69 model.
"""

from math import sqrt, log

def ComputeDistMatrix(aligned_sequences):
    """Reads dictionary of aligned sequence pairs and returns a list of lists
    containing evolutionary distances as a matrix.
    """

    if not ValidAlignment(aligned_sequences):
        raise Exception("malformed input")

    matrix = InitializeDistMatrix(len(aligned_sequences))
    distance_matrix = PairwiseDistance(aligned_sequences, matrix)

    return distance_matrix



def ValidAlignment(aligned_sequences):
    """Reads dictionary of aligned sequence pairs with structure
    (entry1, entry2): (aligned_seq1, aligned_seq2)
    returns True if valid and False otherwise.

    Entry1 and 2 should be integers.

    Aligned_seq1 and 2 ahould be strings, have the same length and
    only containing uppercase A, T, G, C or -.
    """

    valid_nucleotides = "ATGC-"

    if type(aligned_sequences) is not dict:
        return False

    for entry_pair in aligned_sequences:
        if type(entry_pair) is not tuple:
            return False
        if len(entry_pair) != 2:
            return False

        for entry in entry_pair:
            if type(entry) is not int:
                return False

    for sequence_pair in aligned_sequences.values():
        if type(sequence_pair) is not tuple:
            return False
        if len(sequence_pair) != 2:
            return False
        if len(sequence_pair[0]) != len(sequence_pair[1]):
            return False

        for sequence in sequence_pair:
            if type(sequence) is not str:
                return False

            for nucleotide in sequence:
                if nucleotide not in valid_nucleotides:
                    return False

    return True



def InitializeDistMatrix(combinations):
    """Takes an integer and returns a n by n matrix (list of lists) of appropriate
    size filled with None.
    """

    size = int((sqrt(8*combinations+1)+1)/2)
    matrix = [[None for column in range(size)] for row in range(size)]

    return matrix



def PairwiseDistance(aligned_sequences, matrix):
    """Takes aligned sequences and a prepared matrix and returns
    the matrix (list of lists) filled with calculated distances as float.
    """

    # diagonal values compare same sequences, distance is 0.
    for entry in range(0, len(matrix)):
        matrix[entry][entry] = 0.

    # for each alignment the distance (d_dist) is estimated using the JC69 model
    for pair in aligned_sequences:
        nucleotide_total = len(aligned_sequences[pair][0])

        nucleotide_difference = 0
        nucleotide_compared = 0

        for nucleotide in range(0, nucleotide_total):
            entry1_nucleotide = aligned_sequences[pair][0][nucleotide]
            entry2_nucleotide = aligned_sequences[pair][1][nucleotide]

            # for he p_dist computation all gap positions are excluded and only
            # nucleotide differences are considered
            if entry1_nucleotide == "-" or entry2_nucleotide == "-":
                continue
            if entry1_nucleotide != entry2_nucleotide:
                nucleotide_difference += 1
                nucleotide_compared += 1
            if entry1_nucleotide == entry2_nucleotide:
                nucleotide_compared += 1

        p_dist = nucleotide_difference/nucleotide_compared
        d_dist = -3/4*log(1-p_dist*4/3)

        matrix[pair[0]][pair[1]] = d_dist
        matrix[pair[1]][pair[0]] = d_dist

    return matrix


if __name__ == "__main__":
    P2_output = {(0, 1): ("ACCAAACATCCAAACA-CCAAC-CCCAGCC-CTTACGCAATC-ATACAAAGAATATT", "ACCAAACCTGTCCCCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC"),
                 (0, 2): ("ACCA-A-ACATCCAA-AC-ACCAAC-CCCA-GCCCTTA-CGCAATCATACAAAGAATATT", "ACTATACCCACCCAACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC"),
                 (0, 3): ("A--CCAAACATCCA-AACA-CCAACCCCAGCCCTTACGCAATCATA-CAAAGAAT-A--TT", "ACCCCACCCGTCTACACCAGCCAACACCAACCCCCAC-CTACTATACCAACCAATAACCTC"),
                 (0, 4): ("A--CCAAACATCC--AAACACCAACCCCAGCCCTTACGCAATCATACAAA-GAAT-A--TT", "ACCCCATTTATCCATAAAAACCAACACCAACCCCCA-TCTAACACACAAACTAATGACCCC"),
                 (0, 5): ("A--CCAAACATCCA-A-ACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT", "ACCCCATCCACCCATACAAACCAACATTA-CCCAT-C-CAAT-ATACAAA-CACCTC"),
                 (0, 6): ("A--CCAAACATCCA-A-ACACCAACCCCAGCCCT-TACGCAATCATACAAAGAATATT", "ACCCCACTCACCCATACAAACCAACACCA-CTCTCCACCTAAT-ATACAAA-TACCTC"),
                 (1, 2): ("ACCAAACCTGTCC--C-C-ATCTAACACCAACCCACATATA-CAAGCTAAACCAAAAATACC", "ACTATACCCACCCAACTCGACCT-ACACCAATCCCCACATAGCACAC-AGACCAACAACCTC"),
                 (1, 3): ("ACCAAACCTGTC--C-CCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC", "ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC"),
                 (1, 4): ("ACCAAACCTGTCC---CCATCTAACACCAACCCACATAT-ACAAGCTAAACCAAAAATACC", "ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACAC-AAACTAATGACCCC"),
                 (1, 5): ("ACCAAACCTGTCCCCATCTAACACCAAC-CCACATATACAAGCTAAACCAAAAATACC", "ACC--CCATCCACCCATACAA-ACCAACATTACCCATCCAA--TATA-CAAACACCTC"),
                 (1, 6): ("ACCAAACCTGTCCCCATCTAACACCAAC-CCACATATACAAGCTAAACCAAAAATA-C-C", "ACCCCA-CT-CACCCATACAA-ACCAACACCAC-TCT-CCACCTAATATACAAATACCTC"),
                 (2, 3): ("ACTATACCCACCCA-ACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC", "ACCCCACCCGTCTACAC-CAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC"),
                 (2, 4): ("ACTATACCCACCCAACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC", "ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC"),
                 (2, 5): ("ACTATACCCACCCA-ACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC", "ACCCCATCCACCCATAC-AAACC-A-A-C-ATTACC-CAT-CCA-ATATACAAAC-ACCTC"),
                 (2, 6): ("ACTATACCCACCCA-ACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC", "ACCCCACTCACCCATAC-AAACCAACACCACTCTCCACCT---A-ATATA-CAAATACCTC"),
                 (3, 4): ("ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC", "ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC"),
                 (3, 5): ("ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC", "ACCCCATCCACCCATACAAACCAACA-TTA--CCCATCCAATATA-C-A--AA-CACCTC"),
                 (3, 6): ("ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC", "ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATA-C-A--AAT-ACCTC"),
                 (4, 5): ("ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC", "ACCCCATCCACCCATACAAACCAACA-TTA--CCCATCCAATATACAAAC-----ACCTC"),
                 (4, 6): ("ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC", "ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATAC--A--AAT-ACCTC"),
                 (5, 6): ("ACCCCATCCACCCATACAAACCAACATTA--C-CCATCCAATATACAAACACCTC", "ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATACAAATACCTC")}

    print(ComputeDistMatrix(P2_output))

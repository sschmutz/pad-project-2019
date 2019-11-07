"""This module creates a pairwise distance matrix from aligned sequences"""

import math

def ComputeDistMatrix(aligned_sequences):
    """Reads dictionary of aligned sequence pairs and returns a list of lists
    containing evolutionary distances"""

    if not ValidAlignment(aligned_sequences):
        raise Exception("malformed input")

    matrix = InitializeDistMatrix(len(aligned_sequences))

    distance_matrix = PairwiseDistance(aligned_sequences, matrix)

    for row in matrix:
        print(row)

    return distance_matrix



def ValidAlignment(aligned_sequences):
    """Reads dictionary of aligned sequence pairs with structure
    (entry1, entry2): (aligned_seq1, aligned_seq2)
    and returns False if not valid.

    entry1 and 2 should be of type integer

    aligned_seq1 and 2 ahould be of type string, have the same length and
    only containing uppercase A, T, G, C or -

    ?TODO test if all possible combinations are present
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
    size = int((math.sqrt(8*combinations+1)+1)/2)
    matrix = [[None for column in range(size)] for row in range(size)]

    return matrix



def PairwiseDistance(aligned_sequences, matrix):
    return None

P2_output = {(0, 1): ('ACCAAACATCCAAACA-CCAAC-CCCAGCC-CTTACGCAATC-ATACAAAGAATATT', 'ACCAAACCTGTCCCCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC'), (0, 2): ('ACCA-A-ACATCCAA-AC-ACCAAC-CCCA-GCCCTTA-CGCAATCATACAAAGAATATT', 'ACTATACCCACCCAACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC'), (0, 3): ('A--CCAAACATCCA-AACA-CCAACCCCAGCCCTTACGCAATCATA-CAAAGAAT-A--TT', 'ACCCCACCCGTCTACACCAGCCAACACCAACCCCCAC-CTACTATACCAACCAATAACCTC'), (0, 4): ('A--CCAAACATCC--AAACACCAACCCCAGCCCTTACGCAATCATACAAA-GAAT-A--TT', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCA-TCTAACACACAAACTAATGACCCC'), (0, 5): ('A--CCAAACATCCA-A-ACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT', 'ACCCCATCCACCCATACAAACCAACATTA-CCCAT-C-CAAT-ATACAAA-CACCTC'), (0, 6): ('A--CCAAACATCCA-A-ACACCAACCCCAGCCCT-TACGCAATCATACAAAGAATATT', 'ACCCCACTCACCCATACAAACCAACACCA-CTCTCCACCTAAT-ATACAAA-TACCTC'), (1, 2): ('ACCAAACCTGTCC--C-C-ATCTAACACCAACCCACATATA-CAAGCTAAACCAAAAATACC', 'ACTATACCCACCCAACTCGACCT-ACACCAATCCCCACATAGCACAC-AGACCAACAACCTC'), (1, 3): ('ACCAAACCTGTC--C-CCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC', 'ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC'), (1, 4): ('ACCAAACCTGTCC---CCATCTAACACCAACCCACATAT-ACAAGCTAAACCAAAAATACC', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACAC-AAACTAATGACCCC'), (1, 5): ('ACCAAACCTGTCCCCATCTAACACCAAC-CCACATATACAAGCTAAACCAAAAATACC', 'ACC--CCATCCACCCATACAA-ACCAACATTACCCATCCAA--TATA-CAAACACCTC'), (1, 6): ('ACCAAACCTGTCCCCATCTAACACCAAC-CCACATATACAAGCTAAACCAAAAATA-C-C', 'ACCCCA-CT-CACCCATACAA-ACCAACACCAC-TCT-CCACCTAATATACAAATACCTC'), (2, 3): ('ACTATACCCACCCA-ACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC', 'ACCCCACCCGTCTACAC-CAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC'), (2, 4): ('ACTATACCCACCCAACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC'), (2, 5): ('ACTATACCCACCCA-ACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC', 'ACCCCATCCACCCATAC-AAACC-A-A-C-ATTACC-CAT-CCA-ATATACAAAC-ACCTC'), (2, 6): ('ACTATACCCACCCA-ACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC', 'ACCCCACTCACCCATAC-AAACCAACACCACTCTCCACCT---A-ATATA-CAAATACCTC'), (3, 4): ('ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC'), (3, 5): ('ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC', 'ACCCCATCCACCCATACAAACCAACA-TTA--CCCATCCAATATA-C-A--AA-CACCTC'), (3, 6): ('ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC', 'ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATA-C-A--AAT-ACCTC'), (4, 5): ('ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC', 'ACCCCATCCACCCATACAAACCAACA-TTA--CCCATCCAATATACAAAC-----ACCTC'), (4, 6): ('ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC', 'ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATAC--A--AAT-ACCTC'), (5, 6): ('ACCCCATCCACCCATACAAACCAACATTA--C-CCATCCAATATACAAACACCTC', 'ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATACAAATACCTC')}

ComputeDistMatrix(P2_output)

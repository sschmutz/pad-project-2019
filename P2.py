"""This module..."""

def AlignByDP(sequences):
    """Reads list of sequence pairs (label, sequence) and returns a dictionary
    of aligned sequences."""

    if not ValidSequences(sequences):
        raise Exception("malformed input")

    return "finished"


def ValidSequences(sequences):
    """Reads list of sequence pairs (label, sequence) and returns False if not valid.

    sequences should be of type list with length > 0,
    contain tuples of length 2 (both of type string)

    while the first element represents the label without any whitespace character
    the second element should be a nucleotide sequence only containing A, T, G, C
    """

    # TODO: write function

    return True










P1_output = [('Mouse', 'ACCAAACATCCAAACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT'),
             ('Bovine', 'ACCAAACCTGTCCCCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC'),
             ('Gibbon', 'ACTATACCCACCCAACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC'),
             ('Orangutan', 'ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC'),
             ('Gorilla', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC'),
             ('Chimp', 'ACCCCATCCACCCATACAAACCAACATTACCCATCCAATATACAAACACCTC'),
             ('Human', 'ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATACAAATACCTC')]

AlignByDP(P1_output)

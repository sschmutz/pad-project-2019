"""This module uses dynamic programming to align nucleotide sequences"""

def AlignByDP(sequences):
    """Reads list of sequence pairs (label, sequence) and returns a dictionary
    of aligned sequences."""

    if not ValidSequences(sequences):
        raise Exception("malformed input")

    alignments = dict()

    # Compare each pair of the input sequences with eachother
    for entry1 in range(0, len(sequences)-1):
        for entry2 in range(entry1+1, len(sequences)):

            seq1 = P1_output[entry1][1]
            seq2 = P1_output[entry2][1]

            # run alignment function which should return two strings (sequences)
            # aligned to each eachother

            alignments[(entry1, entry2)] = AlignSequences(seq1, seq2)

    return alignments



def ValidSequences(sequences):
    """Reads list of sequence pairs (label, sequence) and returns False if not valid.

    sequences should be of type list,
    contain tuples of length 2 of which both are of type string

    while the first element represents the label without any whitespace character
    the second element should be a nucleotide sequence only containing
    uppercase A, T, G, C
    """

    valid_nucleotides = "ATGC"


    if type(sequences) is not list:
        return False

    for entry in sequences:
        if type(entry) is not tuple:
            return False
        elif len(entry) != 2:
            return False
        elif len(entry[0].split()) > 1:
            return False

        for element in entry:
            if type(element) is not str:
                return False

        for nucleotides in entry[1]:
            for nucleotide in nucleotides:
                if nucleotide not in valid_nucleotides:
                    return False

    return True










P1_output = [("Mouse", "ACCAAACATCCAAACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT"),
             ("Bovine", "ACCAAACCTGTCCCCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC"),
             ("Gibbon", "ACTATACCCACCCAACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC"),
             ("Orangutan", "ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC"),
             ("Gorilla", "ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC"),
             ("Chimp", "ACCCCATCCACCCATACAAACCAACATTACCCATCCAATATACAAACACCTC"),
             ("Human", "ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATACAAATACCTC")]

P1_output_false1 = ("Mouse", "ACCAAACATCCAAACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT")
P1_output_false2 = ["Mouse", "ACCAAACATCCAAACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT"]
P1_output_false3 = [("Mouse", "ACCAAACATCCAAACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT", "t")]
P1_output_false4 = [(1, "ACCAAACATCCAAACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT")]
P1_output_false5 = [("Mouse 1", "ACCAAACATCCAAACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT")]
P1_output_false6 = [("Mouse", "ACCAAACATCCAAACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT"),
                    ("Bovine", "AcCAAACCTGTCCCCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC")]



print(AlignByDP(P1_output))

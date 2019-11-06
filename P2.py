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

            seq1 = sequences[entry1][1]
            seq2 = sequences[entry2][1]

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



def AlignSequences(seq1, seq2):
    """Takes two strings (nucleotide sequences) and returns aligned strings
    in a tuple"""

    match = 5
    mismatch = -2
    indel = -6

    # set up scoring matrix
    matrix = [[None for column in range(len(seq2)+1)] for row in range(len(seq1)+1)]

    rows = len(matrix)
    columns = len(matrix[0])

    possible_paths = []

    # starting value of the matrix is defined as 0
    matrix[0][0] = 0

    # populating first i and j residues of seq1 and seq2
    for row in range(1, rows):
        matrix[row][0] = matrix[row-1][0] + indel
        possible_paths.append(((row-1, 0), (row, 0)))

    for column in range(1, columns):
        matrix[0][column] = matrix[0][column-1] + indel
        possible_paths.append(((0, column-1), (0, column)))

    # populating rest of the matrix
    for row in range(1, rows):
        for column in range(1, columns):

            if seq1[row-1] == seq2[column-1]:
                upper_left = matrix[row-1][column-1] + match
            else:
                upper_left = matrix[row-1][column-1] + mismatch

            above = matrix[row-1][column] + indel
            left = matrix[row][column-1] + indel

            scores = {((row-1, column-1), (row, column)) : upper_left, \
                      ((row-1, column), (row, column)) : above, \
                      ((row, column-1), (row, column)) : left}

            max_score = max(scores.values())

            for path in scores:
                if scores[path] == max_score:
                    possible_paths.append(path)

            matrix[row][column] = max_score

    # traceback following the possible paths
    last_position = [(rows-1, columns-1)]
    seq1_aligned = []
    seq2_aligned = []

    # following part could probably be sped up with a while loop
    for row in range(rows-1, -1, -1):
        for column in range(columns-1, -1, -1):
            if ((row-1, column-1), (row, column)) in possible_paths and (row, column) == last_position[-1]:
                # it's a match or mismatch
                last_position.append((row-1, column-1))

                seq1_aligned.append(seq1[row-1])
                seq2_aligned.append(seq2[column-1])

            elif ((row-1, column), (row, column)) in possible_paths and (row, column) == last_position[-1]:
                # it's an indel
                last_position.append((row-1, column))

                seq1_aligned.append(seq1[row-1])
                seq2_aligned.append("-")

            elif ((row, column-1), (row, column)) in possible_paths and (row, column) == last_position[-1]:
                # it's an indel
                last_position.append((row, column-1))

                seq1_aligned.append("-")
                seq2_aligned.append(seq2[column-1])

    # put alignment in correct order
    seq1_aligned.reverse()
    seq2_aligned.reverse()

    seq1_aligned = "".join(seq1_aligned)
    seq2_aligned = "".join(seq2_aligned)

    return seq1_aligned, seq2_aligned









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

P1_output_simple = [("Mouse", "AAACATCCAAACACCAACCCCAG"),
                    ("Bovine", "ACCAAACCTGTCCCCATCTAACACCA"),
                    ("Gibbon", "AATACCCAACTCGACCTACACCAA")]

P1_output_primer = [("i", "TTCATA"),
                    ("j", "TGCTCGTA")]


print(AlignByDP(P1_output))

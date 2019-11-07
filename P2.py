"""This module uses dynamic programming to align nucleotide sequences"""

def AlignByDP(sequences):
    """Reads list of sequence pairs (label, sequence) and returns a dictionary
    of aligned sequences."""

    if not ValidSequences(sequences):
        raise Exception("malformed input")

    aligned_sequences = dict()

    # align each pair of the input sequences with eachother
    # no alignment is made twice
    for entry1 in range(0, len(sequences)-1):
        for entry2 in range(entry1+1, len(sequences)):

            seq1 = sequences[entry1][1]
            seq2 = sequences[entry2][1]

            aligned_sequences[(entry1, entry2)] = AlignSequences(seq1, seq2)

    return aligned_sequences



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

    # using the method and scoring system as descibed in the
    # Nature Primer publication "What is dynamic programming" by Sean R Eddy
    match = 5
    mismatch = -2
    indel = -6

    matrix = [[None for column in range(len(seq2)+1)] for row in range(len(seq1)+1)]

    rows = len(matrix)
    columns = len(matrix[0])

    # the possible paths for traceback will be saved in a list,
    # there's one element (tuple) for each possible path which consists of
    # two coordinates each (row, column) in tuples
    # for example:
    # ((row from, column from), (row to, column to))
    possible_paths = []

    matrix[0][0] = 0

    # fill in i and j residues of seq1 and seq2 first
    for row in range(1, rows):
        matrix[row][0] = matrix[row-1][0] + indel
        possible_paths.append(((row, 0), (row-1, 0)))

    for column in range(1, columns):
        matrix[0][column] = matrix[0][column-1] + indel
        possible_paths.append(((0, column), (0, column-1)))

    # fill in rest of the matrix by defining the optimum alignment (highest score)
    # through either match, mismatch or indel for each position of the matrix
    for row in range(1, rows):
        for column in range(1, columns):

            if seq1[row-1] == seq2[column-1]:
                upper_left = matrix[row-1][column-1] + match
            else:
                upper_left = matrix[row-1][column-1] + mismatch

            above = matrix[row-1][column] + indel
            left = matrix[row][column-1] + indel

            scores = {((row, column), (row-1, column-1)) : upper_left, \
                      ((row, column), (row-1, column)) : above, \
                      ((row, column), (row, column-1)) : left}

            max_score = max(scores.values())
            matrix[row][column] = max_score

            for path in scores:
                if scores[path] == max_score:
                    possible_paths.append(path)

    # traceback following the possible paths results in the aligned sequences
    last_position = {"row":rows-1, "column":columns-1}
    seq1_aligned = []
    seq2_aligned = []

    # following part could probably be simplified/sped up with a while loop
    for row in range(rows-1, -1, -1):
        for column in range(columns-1, -1, -1):
            if ((row, column), (row-1, column-1)) in possible_paths and (row, column) == (last_position["row"], last_position["column"]):
                # it's a match or mismatch, move to upper left
                last_position["row"] -= 1
                last_position["column"] -= 1

                seq1_aligned.insert(0, seq1[row-1])
                seq2_aligned.insert(0, seq2[column-1])

            elif ((row, column), (row-1, column)) in possible_paths and (row, column) == (last_position["row"], last_position["column"]):
                # it's an indel, move to above
                last_position["row"] -= 1

                seq1_aligned.insert(0, seq1[row-1])
                seq2_aligned.insert(0, "-")

            elif ((row, column), (row, column-1)) in possible_paths and (row, column) == (last_position["row"], last_position["column"]):
                # it's an indel, move to left
                last_position["column"] -= 1

                seq1_aligned.insert(0, "-")
                seq2_aligned.insert(0, seq2[column-1])

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


print(AlignByDP(P1_output_primer))

"""This module uses dynamic programming to align pairs of nucleotide sequences."""



def AlignByDP(sequences):
    """Reads list of sequence pairs (label, sequence) and returns a dictionary
    of aligned sequences.
    """

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
    """Reads list of sequence pairs (label, sequence), returns True if valid
    and False otherwise.

    Sequences should be type list, with length larger than 1,
    contain tuples with length 2 of which both are type string.

    While the first element represents the label the second element should be
    a nucleotide sequence only containing uppercase A, T, G or C.
    """

    valid_nucleotides = ["A", "T", "G", "C"]

    if type(sequences) is not list:
        return False

    if len(sequences) < 2:
        return False

    for entry in sequences:
        if type(entry) is not tuple:
            return False
        if len(entry) != 2:
            return False

        for element in entry:
            if len(element) == 0:
                return False
            if type(element) is not str:
                return False

        for nucleotides in entry[1]:
            for nucleotide in nucleotides:
                if nucleotide not in valid_nucleotides:
                    return False

    return True



def AlignSequences(seq1, seq2):
    """Takes two strings (nucleotide sequences) and returns aligned strings
    in a tuple.

    Using the method and scoring system as descibed in the
    Nature Primer publication "What is dynamic programming" by Sean R Eddy.
    """

    match = 5
    mismatch = -2
    indel = -6

    matrix = [[None for column in range(len(seq2)+1)] for row in range(len(seq1)+1)]

    rows = len(matrix)
    columns = len(matrix[0])

    # the optimal paths for traceback will be saved in a list,
    # there's one element (tuple) for each optimal path which consists of
    # two coordinates each (row, column) stored in tuples
    # for example:
    # ((row from, column from), (row to, column to))
    optimal_paths = []

    matrix[0][0] = 0

    # fill in i and j residues of seq1 and seq2 first
    for row in range(1, rows):
        matrix[row][0] = matrix[row-1][0] + indel
        optimal_paths.append(((row, 0), (row-1, 0)))

    for column in range(1, columns):
        matrix[0][column] = matrix[0][column-1] + indel
        optimal_paths.append(((0, column), (0, column-1)))

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
                    optimal_paths.append(path)

    # traceback following the optimal paths results in the aligned sequences
    # if there are multiple equally optimal paths, one is chosen arbitrarily as follows:
    # upper left > above > left
    last_position = {"row":rows-1, "column":columns-1}
    seq1_aligned = []
    seq2_aligned = []

    while last_position["row"] > 0 or last_position["column"] > 0:
        row = last_position["row"]
        column = last_position["column"]

        if ((row, column), (row-1, column-1)) in optimal_paths:
            # it's a match or mismatch, move to upper left
            seq1_aligned.insert(0, seq1[row-1])
            seq2_aligned.insert(0, seq2[column-1])

            last_position["row"] -= 1
            last_position["column"] -= 1

        elif ((row, column), (row-1, column)) in optimal_paths:
            # it's an indel, move to above
            seq1_aligned.insert(0, seq1[row-1])
            seq2_aligned.insert(0, "-")

            last_position["row"] -= 1

        elif ((row, column), (row, column-1)) in optimal_paths:
            # it's an indel, move to left
            seq1_aligned.insert(0, "-")
            seq2_aligned.insert(0, seq2[column-1])

            last_position["column"] -= 1

    seq1_aligned = "".join(seq1_aligned)
    seq2_aligned = "".join(seq2_aligned)

    return (seq1_aligned, seq2_aligned)


if __name__ == "__main__":
    P1_output = [("Mouse", "ACCAAACATCCAAACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT"),
                 ("Bovine", "ACCAAACCTGTCCCCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC"),
                 ("Gibbon", "ACTATACCCACCCAACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC"),
                 ("Orangutan", "ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC"),
                 ("Gorilla", "ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC"),
                 ("Chimp", "ACCCCATCCACCCATACAAACCAACATTACCCATCCAATATACAAACACCTC"),
                 ("Human", "ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATACAAATACCTC")]

    print(AlignByDP(P1_output))

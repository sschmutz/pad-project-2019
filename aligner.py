seq1 = "TTCATA"
seq2 = "TGCTCGTA"


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


            #scores = [upper_left, above, left]
            #max_score = max(scores)


            matrix[row][column] = max_score

    for row in matrix:
        print(row)

    print(possible_paths)

    # traceback (kinda)
    last_position = [(rows-1, columns-1)]
    seq1_aligned = []
    seq2_aligned = []

    for row in range(rows-1, -1, -1):
        for column in range(columns-1, -1, -1):
            if ((row-1, column-1), (row, column)) in possible_paths and (row, column) == last_position[-1]:
                print("it's a match or mismatch")
                last_position.append((row-1, column-1))

                seq1_aligned.append(seq1[row-1])
                seq2_aligned.append(seq2[column-1])

            elif ((row-1, column), (row, column)) in possible_paths and (row, column) == last_position[-1]:
                # It's an indel!
                print("It's an indel in seq2!")
                last_position.append((row-1, column))

                seq1_aligned.append(seq1[row-1])
                seq2_aligned.append("-")

            elif ((row, column-1), (row, column)) in possible_paths and (row, column) == last_position[-1]:
                # It's an indel!
                print("It's an indel in seq1!")
                last_position.append((row, column-1))

                seq1_aligned.append("-")
                seq2_aligned.append(seq2[column-1])


    # alignment
    seq1_aligned.reverse()
    seq2_aligned.reverse()

    seq1_aligned = "".join(seq1_aligned)
    seq2_aligned = "".join(seq2_aligned)



    #return seq1_aligned, seq2_aligned
    return seq1_aligned, seq2_aligned



print(AlignSequences(seq1, seq2))

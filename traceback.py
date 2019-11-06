# traceback start at last score which was calculated
last_position = [(rows-1, columns-1)]
seq1_aligned = []
seq2_aligned = []
aligned_score = []

for row in range(rows-1, -1, -1):
    for column in range(columns-1, -1, -1):
        if matrix[row][column] - match == matrix[row-1][column-1] and (row, column) == last_position[-1]:
            # It's a match!
            print("It's a match!")
            last_position.append((row-1, column-1))
            print(last_position)

            seq1_aligned.append(seq1[row-1])
            seq2_aligned.append(seq2[column-1])
            aligned_score.append(match)

        elif matrix[row][column] - mismatch == matrix[row-1][column-1] and (row, column) == last_position[-1]:
            # It's a mismatch!
            print("It's a mismatch!")
            last_position.append((row-1, column-1))
            print(last_position)

            seq1_aligned.append(seq1[row-1])
            seq2_aligned.append(seq2[column-1])
            aligned_score.append(mismatch)

        # elif matrix[row][column] - indel == matrix[row-1][column] and (row, column) == last_position[-1]:
        #     # It's an indel!
        #     print("It's an indel in seq2!")
        #     last_position.append((row-1, column))
        #
        #     seq1_aligned.append(seq1[row-1])
        #     seq2_aligned.append("-")
        #     aligned_score.append(indel)
        #
        # elif matrix[row][column] - indel == matrix[row][column-1] and (row, column) == last_position[-1]:
        #     # It's an indel!
        #     print("It's an indel in seq1!")
        #     last_position.append((row, column-1))
        #
        #     seq1_aligned.append("-")
        #     seq2_aligned.append(seq2[row-1])
        #     aligned_score.append(indel)

seq1_aligned.reverse()
seq2_aligned.reverse()
aligned_score.reverse()

print("".join(seq1_aligned))
print("".join(seq2_aligned))
print(aligned_score)

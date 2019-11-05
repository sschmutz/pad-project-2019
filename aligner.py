seq1 = "TTC"
seq2 = "TGC"


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
    
    # starting value of the matrix is defined as 0
    matrix[0][0] = 0

    # populating first i and j residues of seq1 and seq2
    for row in range(1, rows):
        matrix[row][0] = matrix[row-1][0] + indel
        
    for column in range(1, columns):
        matrix[0][column] = matrix[0][column-1] + indel
  
    
    # populating rest of the matrix
    for row in range(1, rows):
        for column in range(1, columns):
            
            if seq1[row-1] == seq2[column-1]:
                diag = matrix[row-1][column-1] + match
            else:
                diag = matrix[row-1][column-1] + mismatch
            
            up = matrix[row-1][column] + indel
            left = matrix[row][column-1] + indel
            
            
            scores = {(row-1, column-1) : diag, (row-1, column) : up, (row, column-1) : left}
            max_score = max(scores.values())

            
            matrix[row][column] = max_score

    print(matrix)
    
    # traceback

    # alignment



    #return seq1_aligned, seq2_aligned
    return seq1, seq2



print(AlignSequences(seq1, seq2))

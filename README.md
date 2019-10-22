# pad-project-2019
>reads genomics sequences from a file and clusters them in a tree according
to their pairwise evolutionary distances

## `P1.py` Parsing a Sequence File
**Prototype:**  
list(tuple(string, string))  
**ParseSeqFile**(string)

### Input
Path and filename pointing to a sequence file

### Output
List of pairs, where each pair consists of a label and the corresponding sequence

## `P2.py` 
**Prototype:**  
dict(tuple(int, int) -> tuple(string, string))  
**AlignByDP**(list(tuple(string, string)))

### Input
The input format corresponds to the output format of P1. But the function should still be
considered self-contained, i.e if the input violates the above type, it should throw an
exception with the message “malformed input”.

### Output
A dictionary. The keys should be tuples of integers (i,j). A key maps to the alignment
of the corresponding sequences from the input. The alignment should be represented as a
tuple (<Aligned Sequence i>, <Aligned Sequence j>).

## `P3.py`  
**Prototype:**  
list(list(float))  
**ComputeDistMatrix**(dict(tuple(int, int) -> tuple(string, string))

### Input
The input format corresponds to the output format of P2. But the function should still
be considered self-contained, i.e if the input violates the above type, it should throw
an exception with the message “malformed input”.

### Output
A symmetrical matrix with zeroes in the diagonal. Each entry i,j corresponds to the
evolutionary distance between sequences i and j.

## `P4.py` 
**Prototype:**  
string  
**Cluster**(list(list(float)), list)

### Input
The input format corresponds to the output format of P3. But the function should still
be considered self-contained, i.e if the input violates the above type, it should throw
an exception with the message “malformed input”.

### Output
A binary tree in string format.

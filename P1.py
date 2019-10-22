"""This module contains code to parse a sequence file"""
# according PEP 257 (see: https://www.python.org/dev/peps/pep-0257/)
# "All modules should normally have docstrings"
# but is it necessary?

# Don't forget to close the file

import os
import sys

def ParseSeqFile(path, filename):
    """Parse a sequence file and return a list of pairs (label, sequence).

    path:       path of directory where the sequence file is located
    filename:   filename (including extension) of the sequence file
    """

    seq_file = ReadSeqFile(path, filename)

    seq_pairs = []

    for line in seq_file:
        if line[0] == ">":
            label = line[1:].split()[0]

            #rewrite nicer
            nucleotide_raw = line[1:].split(maxsplit = 1)[1]
            nucleotide = "".join(nucleotide_raw.split())

            seq_pairs.append((label, nucleotide))
        else:
            #doesn't perform properly yet prints as soon as there's one line
            #not starting with a >?!
            print("malformed input")

    seq_file.close()
    return seq_pairs


def ReadSeqFile(path, filename):
    """Read a sequence file and return it's contents."""

    full_filename = os.path.join(path, filename)

    try:
        seq_file = open(full_filename, "r")
    except:
        sys.exit("Combination of path and filename can't be opened.")

    return(seq_file)




path = "/Users/stefan_schmutz/Documents/GitHub/pad-project-2019/input"
filename = "sequeces_example_1.txt"
print(ParseSeqFile(path, filename))

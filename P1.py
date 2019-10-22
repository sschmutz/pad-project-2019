"""This module contains code to parse a sequence file"""
# according PEP 257 (see: https://www.python.org/dev/peps/pep-0257/)
# "All modules should normally have docstrings"
# but is it necessary?

import os
import sys

def ParseSeqFile(path, filename):
    """Parse a sequence file and return a list of pairs (label, sequence).

    path:       path of directory where the sequence file is located
    filename:   filename (including extension) of the sequence file
    """

    seq_file_content = ReadSeqFile(path, filename)

    if ValidSeqFile(seq_file_content):
        return(seq_file_content)
    else:
        print("malformed input")


def ReadSeqFile(path, filename):
    """Read a sequence file and return it's contents."""

    full_filename = os.path.join(path, filename)

    try:
        seq_file = open(full_filename, "r")
    except:
        sys.exit("Combination of path and filename can't be opened.")

    seq_file_content = seq_file.read()
    seq_file.close()
    return(seq_file_content)


def ValidSeqFile(seq_file_content):
    """Go through sequence file contents and check for validity."""

    valid_lines = 0

    for line in seq_file_content:
        if line[0] == ">":
            valid_lines += 1

    if valid_lines > 0:
        return True
    else:
        return False





path = "/Users/stefan_schmutz/Documents/GitHub/pad-project-2019/input"
filename = "sequeces_example_1.txt"
print(ParseSeqFile(path, filename))

# wrong or missing path
print(ParseSeqFile("wrong path", filename))

"""This module reads labels and sequences from a text file."""

import os
import sys



def ParseSeqFile(path, filename):
    """Parse a sequence file and return a list of pairs (label, sequence).

    path:       path of directory where the sequence file is located
    filename:   filename (including extension) of the sequence file
    """

    seq_file = OpenSeqFile(path, filename)
    seq_pairs = []

    for line in seq_file:
        if ValidSeq(line):
            seq_pairs.append(ValidSeq(line))

    seq_file.close()

    if seq_pairs:
        return seq_pairs

    # only raises exception if no line contains a valid sequence pair
    raise Exception("malformed input")



def OpenSeqFile(path, filename):
    """Opens a sequence file if possible and returns it."""

    try:
        full_filename = os.path.join(path, filename)
        seq_file = open(full_filename, "r")
    except FileNotFoundError:
        print("Combination of path and filename can't be opened.")
        raise

    return seq_file



def ValidSeq(line):
    """Read line from SeqFile and return matching label and sequence in a tuple.

    Checks format of line from sequence file, strips all whitespace characters
    and only returns the label and nucleotide sequence if formatted properly:
        - Line starts with a ">" character
        - First item is present (label)
        - Second item is present (nucleotide sequence consisting of A, T, G or C)

    Returns "None" if the line isn't valid.
    """

    if line[0] == ">":

        try:
            # Per definition, the first element after the ">" sign is the label
            label = line[1:].split()[0]

            # Extract everything after the label and return upper case letters
            nucleotides_raw = line[1:].split(maxsplit=1)[1].upper()
            # Remove all whitespace characters from the nucleotide sequence
            nucleotides = "".join(nucleotides_raw.split())
        except ValueError:
            return None

        # We only deal with upper case nucleotide letters
        valid_nucleotides = "ATGC"

        for nucleotide in nucleotides:
            if nucleotide not in valid_nucleotides:
                return None

        return (label, nucleotides)



PATH = "/Users/stefan_schmutz/Documents/GitHub/pad-project-2019/input"
FILENAME = "sequeces_example_1.txt"
print(ParseSeqFile(PATH, FILENAME))

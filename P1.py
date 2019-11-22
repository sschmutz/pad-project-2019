"""This module reads labels and sequences from a text file."""



def ParseSeqFile(path_filename):
    """Takes a filepath as string, parses the containing sequences
    and returns a list of tuple pairs as string (label, sequence).
    """

    seq_file = open(path_filename, "r")
    seq_pairs = []

    for line in seq_file:
        valid_line = ValidSeq(line)

        if valid_line:
            seq_pairs.append(valid_line)

    seq_file.close()

    if len(seq_pairs) > 0:
        return seq_pairs
    else:
        raise Exception("malformed input")



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


if __name__ == "__main__":
    path_filename = "/Users/stefan_schmutz/Documents/GitHub/pad-project-2019/input/sequeces_example.txt"

    print(ParseSeqFile(path_filename))

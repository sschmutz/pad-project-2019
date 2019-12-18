"""This module reads labels and corresponding sequences from a text file."""



def ParseSeqFile(filepath):
    """Takes a filepath as string, parses the containing sequences
    and returns a list of tuples which contain pairs of (label, sequence)
    as strings.
    """

    seq_file = open(filepath, "r")
    seq_pairs = []

    for line in seq_file:
        valid_line = ValidSeq(line)

        if valid_line:
            seq_pairs.append(valid_line)

    seq_file.close()

    if not seq_pairs:
        raise Exception("malformed input")

    return seq_pairs



def ValidSeq(line):
    """Reads line from a Sequence File and returns matching label and sequence
    as strings in a tuple.

    Checks format of line from sequence file, strips all whitespace characters
    and only returns the label and nucleotide sequence if formatted properly:
        - Line starts with a ">" character
        - First item is present (label)
        - Second item is present (nucleotide sequence consisting of only A, T, G or C)

    Returns None if the line isn't valid.
    """

    if line[0] == ">":

        try:
            # Per definition, the first element after the ">" sign is the label
            label = line[1:].split()[0]

            # Extract everything after the label which is the nucleotide sequence
            nucleotides_raw = line[1:].split(maxsplit=1)[1].upper()
            # Remove all whitespace characters within the nucleotide sequence
            nucleotides = "".join(nucleotides_raw.split())
        except:
            return None

        valid_nucleotides = ["A", "T", "G", "C"]

        for nucleotide in nucleotides:
            if nucleotide not in valid_nucleotides:
                return None

        return (label, nucleotides)



if __name__ == "__main__":
    filepath = "./input/sequences_example.txt"

    print(ParseSeqFile(filepath))

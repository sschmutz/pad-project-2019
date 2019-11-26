import P1
import pytest

def test_ParseSeqFile():
    P1_output = P1.ParseSeqFile("./input/sequences_example.txt")
    P1_output_expected = [('Mouse', 'ACCAAACATCCAAACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT'),
                          ('Bovine', 'ACCAAACCTGTCCCCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC'),
                          ('Gibbon', 'ACTATACCCACCCAACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC'),
                          ('Orangutan', 'ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC'),
                          ('Gorilla', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC'),
                          ('Chimp', 'ACCCCATCCACCCATACAAACCAACATTACCCATCCAATATACAAACACCTC'),
                          ('Human', 'ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATACAAATACCTC')]

    assert P1_output == P1_output_expected

def test_Fails():
    # no valid line
    with pytest.raises(Exception, match="malformed input"):
        P1.ParseSeqFile("./input/sequences_fail1.txt")

    # label consists of more than one word
    with pytest.raises(Exception, match="malformed input"):
        P1.ParseSeqFile("./input/sequences_fail2.txt")

    # invalid nucleotide letter
    with pytest.raises(Exception, match="malformed input"):
        P1.ParseSeqFile("./input/sequences_fail3.txt")

    # no nucleotide sequence
    with pytest.raises(Exception, match="malformed input"):
        P1.ParseSeqFile("./input/sequences_fail4.txt")

def test_SpecialCases():
    # label is an integer
    P1_output_1 = P1.ParseSeqFile("./input/sequences_special1.txt")
    P1_output_expected_1 = [('1', 'ACCCCATTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC')]

    assert P1_output_1 == P1_output_expected_1

    # one sequence missing
    P1_output_2 = P1.ParseSeqFile("./input/sequences_special2.txt")
    P1_output_expected_2 = [('Gorilla', 'ACCCCATTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC')]

    assert P1_output_2 == P1_output_expected_2

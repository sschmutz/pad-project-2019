import P2
import pytest

def test_AlignByDP():
    P1_output = [('Mouse', 'ACCAAACATCCAAACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT'),
                 ('Bovine', 'ACCAAACCTGTCCCCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC'),
                 ('Gibbon', 'ACTATACCCACCCAACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC'),
                 ('Orangutan', 'ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC'),
                 ('Gorilla', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC'),
                 ('Chimp', 'ACCCCATCCACCCATACAAACCAACATTACCCATCCAATATACAAACACCTC'),
                 ('Human', 'ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATACAAATACCTC')]
    P2_output = P2.AlignByDP(P1_output)
    P2_output_expected = {(0, 1): ('ACCAAACATCCAAACA-CCAAC-CCCAGCC-CTTACGCAATC-ATACAAAGAATATT', 'ACCAAACCTGTCCCCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC'),
                          (0, 2): ('ACCA-A-ACATCCAA-AC-ACCAAC-CCCA-GCCCTTA-CGCAATCATACAAAGAATATT', 'ACTATACCCACCCAACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC'),
                          (0, 3): ('A--CCAAACATCCA-AACA-CCAACCCCAGCCCTTACGCAATCATA-CAAAGAAT-A--TT', 'ACCCCACCCGTCTACACCAGCCAACACCAACCCCCAC-CTACTATACCAACCAATAACCTC'),
                          (0, 4): ('A--CCAAACATCC--AAACACCAACCCCAGCCCTTACGCAATCATACAAA-GAAT-A--TT', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCA-TCTAACACACAAACTAATGACCCC'),
                          (0, 5): ('A--CCAAACATCCA-A-ACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT', 'ACCCCATCCACCCATACAAACCAACATTA-CCCAT-C-CAAT-ATACAAA-CACCTC'),
                          (0, 6): ('A--CCAAACATCCA-A-ACACCAACCCCAGCCCT-TACGCAATCATACAAAGAATATT', 'ACCCCACTCACCCATACAAACCAACACCA-CTCTCCACCTAAT-ATACAAA-TACCTC'),
                          (1, 2): ('ACCAAACCTGTCC--C-C-ATCTAACACCAACCCACATATA-CAAGCTAAACCAAAAATACC', 'ACTATACCCACCCAACTCGACCT-ACACCAATCCCCACATAGCACAC-AGACCAACAACCTC'),
                          (1, 3): ('ACCAAACCTGTC--C-CCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC', 'ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC'),
                          (1, 4): ('ACCAAACCTGTCC---CCATCTAACACCAACCCACATAT-ACAAGCTAAACCAAAAATACC', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACAC-AAACTAATGACCCC'),
                          (1, 5): ('ACCAAACCTGTCCCCATCTAACACCAAC-CCACATATACAAGCTAAACCAAAAATACC', 'ACC--CCATCCACCCATACAA-ACCAACATTACCCATCCAA--TATA-CAAACACCTC'),
                          (1, 6): ('ACCAAACCTGTCCCCATCTAACACCAAC-CCACATATACAAGCTAAACCAAAAATA-C-C', 'ACCCCA-CT-CACCCATACAA-ACCAACACCAC-TCT-CCACCTAATATACAAATACCTC'),
                          (2, 3): ('ACTATACCCACCCA-ACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC', 'ACCCCACCCGTCTACAC-CAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC'),
                          (2, 4): ('ACTATACCCACCCAACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC'),
                          (2, 5): ('ACTATACCCACCCA-ACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC', 'ACCCCATCCACCCATAC-AAACC-A-A-C-ATTACC-CAT-CCA-ATATACAAAC-ACCTC'),
                          (2, 6): ('ACTATACCCACCCA-ACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC', 'ACCCCACTCACCCATAC-AAACCAACACCACTCTCCACCT---A-ATATA-CAAATACCTC'),
                          (3, 4): ('ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC'),
                          (3, 5): ('ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC', 'ACCCCATCCACCCATACAAACCAACA-TTA--CCCATCCAATATA-C-A--AA-CACCTC'),
                          (3, 6): ('ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC', 'ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATA-C-A--AAT-ACCTC'),
                          (4, 5): ('ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC', 'ACCCCATCCACCCATACAAACCAACA-TTA--CCCATCCAATATACAAAC-----ACCTC'),
                          (4, 6): ('ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC', 'ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATAC--A--AAT-ACCTC'),
                          (5, 6): ('ACCCCATCCACCCATACAAACCAACATTA--C-CCATCCAATATACAAACACCTC', 'ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATACAAATACCTC')}

    assert P2_output == P2_output_expected
    assert len(P2_output) == len(P1_output)*(len(P1_output)-1)/2

def test_InDel():
    P1_output = [('1', 'ACCAAA'),
                 ('2', 'ACCAA'),
                 ('3', 'CCAAA'),
                 ('4', 'ACC')]
    P2_output = P2.AlignByDP(P1_output)
    P2_output_expected = {(0, 1): ('ACCAAA', 'ACC-AA'),
                          (0, 2): ('ACCAAA', '-CCAAA'),
                          (0, 3): ('ACCAAA', 'ACC---'),
                          (1, 2): ('ACCAA', 'CCAAA'),
                          (1, 3): ('ACCAA', 'ACC--'),
                          (2, 3): ('CCAAA', '--ACC')}

    assert P2_output == P2_output_expected

def test_Fails():
    # input not a list
    with pytest.raises(Exception, match="malformed input"):
        P2.AlignByDP("")

    # list with length 0
    with pytest.raises(Exception, match="malformed input"):
        P2.AlignByDP([])

    # list with string not tuple
    with pytest.raises(Exception, match="malformed input"):
        P2.AlignByDP([""])

    # list with emty tuple
    with pytest.raises(Exception, match="malformed input"):
        P2.AlignByDP([()])

    # list with tuple of length != 2
    with pytest.raises(Exception, match="malformed input"):
        P2.AlignByDP([("Human", "ATG", "ATG"), ("Human", "ATG")])

    # label has length 0
    with pytest.raises(Exception, match="malformed input"):
        P2.AlignByDP([("", "ATG"), ("Human", "ATG")])

    # sequence has length 0
    with pytest.raises(Exception, match="malformed input"):
        P2.AlignByDP([("Human", ""), ("Human", "ATG")])

    # only one sequence
    with pytest.raises(Exception, match="malformed input"):
        P2.AlignByDP([("Human", "ATG")])

    # not a valid nucleotide
    with pytest.raises(Exception, match="malformed input"):
        P2.AlignByDP([("Human", "ATG"), ("Human", "ATg")])

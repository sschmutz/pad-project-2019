import unittest
import os
import P1

class TestP1(unittest.TestCase):

    def test_ParseSeqFile(self):
        path = "/Users/stefan_schmutz/Documents/GitHub/pad-project-2019/input/"
        P1_output = P1.ParseSeqFile(os.path.join(path, "sequeces_example.txt"))
        P1_output_expected = [('Mouse', 'ACCAAACATCCAAACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT'),
                              ('Bovine', 'ACCAAACCTGTCCCCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC'),
                              ('Gibbon', 'ACTATACCCACCCAACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC'),
                              ('Orangutan', 'ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC'),
                              ('Gorilla', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC'),
                              ('Chimp', 'ACCCCATCCACCCATACAAACCAACATTACCCATCCAATATACAAACACCTC'),
                              ('Human', 'ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATACAAATACCTC')]

        self.assertListEqual(P1_output, P1_output_expected)

if __name__ == "__main__":
    unittest.main()

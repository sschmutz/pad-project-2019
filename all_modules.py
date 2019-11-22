"""This module combines all modules for the PAD project."""

import P1
import P2
import P3
import P4

print("Module P1 --------------------------------------------")
path_file = "/Users/stefan_schmutz/Documents/GitHub/pad-project-2019/input/sequeces_example_1.txt"
P1_output = P1.ParseSeqFile(path_file)
print(P1_output)

print("Module P2 --------------------------------------------")
P2_output = P2.AlignByDP(P1_output)
print(P2_output)

print("Module P3 --------------------------------------------")
P3_output = P3.ComputeDistMatrix(P2_output)
print(P3_output)

print("Module P4 --------------------------------------------")
P3_output_labels = ["Mouse", "Bovine", "Gibbon", "Orangutan", "Gorilla", "Chimp", "Human"]
P4_output = P4.Cluster(P3_output, P3_output_labels)
print(P4_output)

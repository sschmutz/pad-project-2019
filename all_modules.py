"""This module combines all modules for the PAD project."""

import P1
import P2
import P3
import P4

print("\nModule P1 --------------------------------------------\n")
path_filename = "./input/sequeces_example.txt"
P1_output = P1.ParseSeqFile(path_filename)
print(P1_output)

print("\nModule P2 --------------------------------------------\n")
P2_output = P2.AlignByDP(P1_output)
print(P2_output)

print("\nModule P3 --------------------------------------------\n")
P3_output = P3.ComputeDistMatrix(P2_output)
print(P3_output)

print("\nModule P4 --------------------------------------------\n")
P3_output_labels = ["Mouse", "Bovine", "Gibbon", "Orangutan", "Gorilla", "Chimp", "Human"]
P4_output = P4.Cluster(P3_output, P3_output_labels)
print(P4_output)

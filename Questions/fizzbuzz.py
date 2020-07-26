
# The Problem
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a
# string is the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is
# "ATGCTTCAGAAAGGTCTTACG."
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and
#  'T' occur in s.
# Sample Dataset:
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

sample = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

A = []
C = []
G = []
T = []

for x in sample:
    if x == "A":
        A.append(x)
    elif x == "C":
        C.append(x)
    elif x == "G":
        G.append(x)
    elif x == "T":
        T.append(x)


a_length = len(A)
c_length = len(C)
g_length = len(G)
t_length = len(T)

print(a_length, c_length, g_length, t_length)








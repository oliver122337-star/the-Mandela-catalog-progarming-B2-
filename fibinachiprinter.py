
"""
Filename: fibinachiprint.py
Author: <Hensel, Oliver>
Created: <11/19/2026>
Instructor: Burgess

"""


def n_fibonacci():
    n = input("Enter a non-negative whole number: ")
    n = int(n)
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    print(sequence)
n_fibonacci()
#hi


"""
Filename: factoralcalc.py
Author: <Hensel, Oliver>
Created: <11/19/2026>
Instructor: Burgess

"""


def factor():

    wholenum = input("Enter a non-negative whole number: ")
    num = int(wholenum)
    if num == 0:
        print("0! = 1")
        return 1
    result = 1
    sequence = []
    for i in range(num, 0, -1):
        result *= i
        sequence.append(str(i))
    sequence_str = " * ".join(sequence)
    print(f"{num}! = {sequence_str} = {result}")
    return result
factor()


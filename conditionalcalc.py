"""
Filename: calculator.py
Author: <Hensel, Oliver>
Created: <09/8/2026>
Instructor: Burgess

"""

print("hello,this is required for the assignment\nwelcome to calculator\nrules: only adding, subtracting, multiplying, and dividing is supported\ndo not type \"add,subtract,multiply,or divide \"instead type\"+,-,*,/\"")
n1=input("please enter your first number:")
n2=input("now enter your second number second number:")
sign=input("now the operation/sign:")

n1=int(n1)
n2=int(n2)

if sign=="+":
    print(n1,"+",n2,"=",n1+n2)
    print("thank you for using this")

elif sign=="-":

        print(n1,"-",n2,"=",n1-n2)
        print("thank you for using this")

elif sign=="*":
        print(n1,"*",n2,"=",n1*n2)
        print("thank you for using this")

elif sign=="/":
        print(n1,"/",n2,"=",n1/n2)
        print("thank you for using this")

else:
    print("sorry",sign,"is not supported. maybe try \"+,-,*,/\"")


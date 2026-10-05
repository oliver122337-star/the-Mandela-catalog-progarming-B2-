"""
Filename:  quizgame.py
Author: <Hensel, Oliver>
Created: <09/30/2026>
Instructor: Burgess

"""



score = 0
intro1=input("hello, this is a trivia game \ni will ask 10 questions then grade you at the end. type \'yes\' if you would like to continue")=="yes"

print("alright")
print("question one\n what color is grass?\nA)green\nB)yellow")
q1=input("please enter your answer by typing a or b. do NOT use capitals (it'll break the code, dont do it please)")

if q1=="a":
    score = score+1
elif q1=="b":
    score = score+0
pass

print("question two\n what does \"CPU\" stand for?")

q2=input("a: computer processing univerity \n b: central processing unit")

if q2=="a":
    score = score+0
elif q2=="b":
    score = score+1
pass

print("question three\n Which component is considered the primary \"brain\" of the computer, responsible for executing instructions and processing data?")
q3=input("a: ram \n b: cpu")

if q3=="a":
    score = score+0
elif q3=="b":
    score = score+1
pass


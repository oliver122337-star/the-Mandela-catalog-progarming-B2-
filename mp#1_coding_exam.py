"""
Filename:  mp1#1_coding_exam.py
Author: <Hensel, Oliver>
Created: <09/30/2026>
Instructor: Burgess

"""


score=input("Enter your score: ")

if int(score)>=90:
    print("grade A \n good job! keep up the good work!")
elif int(score)>=80:
    print("grade B \n good job! try just a bit harder next time!")
elif int(score)>=70:
    print("grade C \n uh oh, maybe focus on studying more.")
elif int(score)>=60:
    print("grade D \n watch out, your score is pretty low.")
elif int(score)<60:
    print("grade F \n please retake this test")
else:
    print("if you see this one of us messed up")
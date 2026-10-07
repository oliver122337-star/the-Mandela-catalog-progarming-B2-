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

print("question four\n Which of the following is classified as system software rather than application software?")
q4=input("a: microsoft windows \n b: microsoft word")

if q4=="a":
    score = score+1
elif q4=="b":
    score = score+0
pass

print("question five\n Which operating system is widely recognized for being open-source and serves as the foundation for the Android mobile platform?")
q5=input("a: linux \n b: microsoft windows")

if q5=="a":
    score = score+1
elif q5=="b":
    score = score+0
pass

print("question six\n Who is credited with inventing the World Wide Web in 1989 while working at CERN?")
q6=input("a: bill gates \n b: tim breners-lee")

if q6=="a":
    score = score+0
elif q6=="b":
    score = score+1
pass

print("question seven\n Which storage technology uses mechanical magnetic platters and a moving actuator arm to read and write data?")
q7=input("a: solid state drive \n b: hard disk drive")

if q7=="a":
    score = score+0
elif q7=="b":
    score = score+1
pass

print("question eight\n What term describes software whose original source code is publicly accessible and can be freely modified or shared by anyone?")
q8=input("a: proprietary software \n b: open source software")

if q8=="a":
    score = score+0
elif q8=="b":
    score = score+1
pass
print("question nine\n Which type of user interface uses visual elements like icons, buttons, windows, and pointers rather than text strings?")
q9=input("a: graphical user interface \n b: command line interface")

if q9=="a":
    score = score+1
elif q9=="b":
    score = score+0
pass

print("question ten\n What was the name of the pioneering packet-switching network funded by the U.S. Department of Defense's Advanced Research Projects Agency?")
q10=input("a: ENIAC \n b: ARPANET")

if q10=="a":
    score = score+0
elif q10=="b":
    score = score+1
pass


print("alright, that was the last question. your score was ", score,"/10")



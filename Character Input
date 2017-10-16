"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.




Extras:

1 - Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.

2 - Print out that many copies of the previous message on separate lines.
"""



#https://docs.python.org/2/library/datetime.html#datetime.datetime.now

import datetime
year = int (datetime.datetime.now().year) #Current year

name = input ("Please enter your name: ")
age = int (input ("How old will you be by the end of the year: "))

year_you_turn_100 = str ((year - age+1 + 100))

sentence = name + ", you will turn 100 years old in " + year_you_turn_100 + ". "
print (sentence)



#Extra 1
numOfCopies = int (input("Please enter a number: "))

print (numOfCopies * sentence)



#Extra 2
sentence = sentence + "\n"

print (numOfCopies * sentence)

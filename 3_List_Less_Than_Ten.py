"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.




Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.

XWrite this in one line of Python.X

Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
"""


list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for num in list_1:
  if num < 5:
    print (num)








#Extra 1

"""
Following is the syntax for append() method:

list.append(obj)
Parameters
obj -- This is the object to be appended in the list.
"""

list_2 = []
for num in list_1:
  if num < 5:
    list_2.append (num)
print (list_2)


#Extra 2
#XXX


#Extra 3

the_number = int(input("Please enter a number: "))

list_3 = []
for x in list_1:
  if x < the_number:
    list_3.append (x)
print (list_3)

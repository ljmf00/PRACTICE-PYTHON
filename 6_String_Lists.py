"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""




"""
>>> s = "foobar"
>>> list(s)
['f', 'o', 'o', 'b', 'a', 'r']
You need list
"""

list1 = list(input(": "))

"""
Slicing - the Pythonic and the most recommended method.

l = [1,2,3,4,5]
print l[::-1]
 
>>> [5,4,3,2,1]
"""

list1_inv = list1[::-1]


if list1 == list1_inv:
  print ("This string is a palindrome!")
else:
  print ("This string is NOT a palindrome!")

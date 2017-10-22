"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
XWrite this in one line of PythonX
"""

list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list_res = []

for x in list_1:
  for y in list_2:
    if x == y:
      list_res.append(x)
      
print (list_res)


#Extra 1

import random

"""
random.randint(a, b)
Return a random integer N such that a <= N <= b.

random.randint(1, 10)  # Integer from 1 to 10, endpoints included
"""

rnd_list_1 = []
rnd_list_2 = []
lenght1 = random.randint(1, 20)
lenght2 = random.randint(1, 20)

i=1
while i <= lenght1:
  rnd_list_1.append(random.randint(1,100))
  i += 1
  
j=1
while j <= lenght2:
  rnd_list_2.append(random.randint(1,100))
  j += 1
  
#print (rnd_list_1)
#print (rnd_list_2)

list_common = []

for a in rnd_list_1:
  for b in rnd_list_2:
    if a == b:
      list_common.append(a)
      
print (list_common)

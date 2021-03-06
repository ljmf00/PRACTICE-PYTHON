"""
This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (WITHOUT DUPLICATES). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

The original formulation of this exercise said to write the solution using one line of Python, but a few readers pointed out that this was impossible to do without using sets that I had not yet discussed on the blog, so you can either choose to use the original directive and read about the set command in Python 3.3, or try to implement this on your own and use at least one list comprehension in the solution.

Extra:

Randomly generate two lists to test this
"""
#Extra 1
import random

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

"""
A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it. For example, this listcomp combines the elements of two lists if they are not equal:

>>>
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
"""

"""
>>> t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
>>> t
[1, 2, 3, 1, 2, 5, 6, 7, 8]
>>> list(set(t))
[1, 2, 3, 5, 6, 7, 8]
"""

list_1 = list(set(rnd_list_1))
list_2 = list(set(rnd_list_2))
#print(list_1)
#print(list_2)

if len(list_1) >= len(list_2):
  longer_list = list_1
  shorter_list = list_2
else:
  longer_list = list_2
  shorter_list = list_1
  
#common = [x for x in longer_list for y in shorter_list if x == y]
print([x for x in longer_list for y in shorter_list if x == y])

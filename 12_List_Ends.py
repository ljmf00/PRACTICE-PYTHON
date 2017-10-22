"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. XFor practice, write this code inside a function.X
"""

a = [5, 10, 15, 20, 25]
new = []

"""
list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
"""
new.append(a.pop(0))
new.append(a.pop())
print(new)

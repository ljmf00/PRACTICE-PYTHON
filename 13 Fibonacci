"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. xTake this opportunity to think about how you can use functions.x Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci sequence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

how_many = int(input("How many numbers in the Fibonnaci sequence do you want to generate??\n:"))
nums = []

if how_many==1:
  nums.append(1)
  
if how_many==2:
  nums.append(1)
  nums.append(1)
  
if how_many>=3:
  first = second = 1
  nums.append(first)
  nums.append(second)
  i=1
  
  while i <= (how_many-2):
    new=first+second
    nums.append(new)
    first=second
    second=new
    i+=1
  
print(nums)

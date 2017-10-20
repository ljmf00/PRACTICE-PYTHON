"""
Ask the user for a number and determine whether the number is prime or not. You can (and should!) use your answer to Exercise 4 to help you. XTake this opportunity to practice using functions, described below.X
"""
#A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

num = int(input("Please enter a number (from 2 to +infinity)\n: "))

list = []
i = 1
while i <= num:
  if num % i == 0:
    list.append(i)
  i+=1
  
if len(list)==2:
  print("\n\n" + str(num) + " IS A PRIME!")
else:
  print("\n\n" + str(num) + " is not a prime.")

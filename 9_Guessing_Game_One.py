"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)


Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
#random.randint(a, b)
#Return a random integer N such that a <= N <= b.



import random
num = random.randint(1, 9)
#print (num)

num_guesses = 0

while True:
  guess = (input("\nGuess the number (between 1 and 9)\n:"))
  if guess == "exit":
    print("Number of guesses: " + str(num_guesses))
    break
  else:
    guess_int = int(guess)
    if guess_int == num:
      print ("You're a genius!!! :D")
      print("Number of guesses: " + str(num_guesses))
      break
    elif guess_int < num:
      print ("Too low...try again.")
      num_guesses += 1
    elif guess_int > num:
      print ("Too high...try again.")
      num_guesses += 1

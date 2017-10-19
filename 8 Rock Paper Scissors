"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
i = 0



def draw():
  print("\nDRAW!!!")
  

def win(winner):
  print("\n" + winner + " WINS!!!")


#def ask():
#  question = input("\nDo you want to start a new game? Y/n")
#  if question == "n":
#    break
    


while i < 1:
  p1 = input("\nPlayer 1,\n\nrock,\npaper\nor\nscissors??\n:")
  p2 = input("\nPlayer 2,\n\nrock,\npaper\nor\nscissors??\n:")
  if (p1 == "rock" and p2 == "rock") or (p1 == "paper" and p2 == "paper") or (p1 == "scissors" and p2 == "scissors"):
    draw()
    question = input("\nDo you want to start a new game? Y/n")
    if question == "n":
      break
  elif p1 == "rock":
    if p2 == "paper":
      win("PLAYER2")
      question = input("\nDo you want to start a new game? Y/n")
    if question == "n":
      break
    elif p2 == "scissors":
      win("PLAYER1")
      question = input("\nDo you want to start a new game? Y/n")
    if question == "n":
      break
  elif p1 == "paper":
    if p2 == "rock":
      win("PLAYER1")
      question = input("\nDo you want to start a new game? Y/n")
    if question == "n":
      break
    elif p2 == "scissors":
        win("PLAYER2")
        question = input("\nDo you want to start a new game? Y/n")
    if question == "n":
      break
  elif p1 == "scissors":
    if p2 == "rock":
      win("PLAYER2")
      question = input("\nDo you want to start a new game? Y/n")
    if question == "n":
      break
    elif p2 == "paper":
        win("PLAYER1")
        question = input("\nDo you want to start a new game? Y/n")
    if question == "n":
      break

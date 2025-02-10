#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  playagain = ("Y")
  while playagain == "Y":
    #Create a loop that continues as long as the user wants to play.
    #User can play as many games as they wish.

    #Randomly choose the computer between 'R', 'P', or 'S'
    computer = random.choice(["R", "P", "S"])
    player = input("Choose R, P, or S: ")
    #Prompt the user for their RPS selection
    #Determine winner and state what happened to the user
    if computer == "R":
      print("Computer chose Rock.")
    elif computer == "S":
      print("Computer chose Scissors.")
    else:
      print("Computer chose Paper.")

    if player == "R":
      print("Player chose Rock.")
    elif player == "S":
      print("Player chose Scissors.")
    else:
      print("Player chose Paper.")

    if player == "P" and computer == "S":
      print("Haha you lose!")
      losses = losses +1
    if player == "S" and computer == "R":
      print("Haha you lose!")
      losses = losses +1
    if player == "R" and computer == "P":
      print("Haha you lose!")
      losses = losses +1

    if player == "R" and computer == "S":
      print("Yippee! Hooray! You did it!")
      wins = wins + 1
    if player == "P" and computer == "R":
      print("Yippee! Hooray! You did it!")
      wins = wins + 1
    if player == "S" and computer == "P":
      print("Yippee! Hooray! You did it!")
      wins = wins + 1

    if player == computer:
      print("Heh. i guess we'll call it a draw.")
      ties = ties + 1

    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties , "\t", losses)

    playagain = input("Play Again? (Y/N): ")
  #Ask the user if they would like to play again.
  if playagain == "N":
    print("See ya later bud") 
  #In the end, print the stats
    

if __name__ == '__main__':
  main()

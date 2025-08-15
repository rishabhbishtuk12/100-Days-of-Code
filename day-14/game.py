from getpass import getpass as input

print(" E P I C   ✂   B A T T L E ")

Player1 = input("P1 Select your move (R, P or S) ")
if Player1 == "r" or Player1 == "R" or Player1 == "p" or Player1 == "P" or Player1 == "s" or Player1 == "S" :
  Player2 = input("P2 Select your move (R, P or S) ")
  if Player2 == "r" or Player2 == "R" or Player2 == "p" or Player2 == "P" or Player2 == "s" or Player2 == "S" :
    if (Player1 == "R" or  Player1 == "r") and (Player2 == "S" or  Player2 == "s"):
      print("Player 1 Win")
    elif  (Player1 == "R" or  Player1 == "r") and (Player2 == "P" or  Player2 == "P"):
      print("Player 2 Win")
    elif  (Player1 == "P" or  Player1 == "p") and (Player2 == "S" or  Player2 == "s"):
      print("Player 2 Win")
    elif  (Player1 == "P" or  Player1 == "p") and (Player2 == "R" or  Player2 == "r"):
      print("Player 1 Win")
    elif  (Player1 == "S" or  Player1 == "s") and (Player2 == "R" or  Player2 == "r"):
      print("Player 2 Win")
    elif  (Player1 == "S" or  Player1 == "s") and (Player2 == "P" or  Player2 == "p"):
      print("Player 1 Win")
    else :
      print("It's a Tie")
  else :
    print("wrong input")
else :
  print("wrong input")
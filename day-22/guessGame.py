import random
print("Welcome to Guess Number Game")
print()
print("You have to Guess the in between  to 4000. I will tell you the number is low or high according to your guess ")

correctNumber = random.randint(0,4000)
at = 1
while True:
  guessNumber = int (input("\nGuess the Number : "))
  if (guessNumber > correctNumber ) :
    print("Too High. Try again! ")
    at = at + 1
  
  elif (guessNumber < correctNumber):
    print("TOO Low. Try again! ")
    at = at + 1
  
  elif (guessNumber == correctNumber):
    print("\n That's Correct !")
    print()
    break
  
  else:
    print("That's not a number.")

print("It took you", at , "attempts to guess the number" )
  
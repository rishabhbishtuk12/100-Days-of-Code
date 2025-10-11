def rollSides(sides):
    diceNumber = random.randint(0, sides)
    return diceNumber

def mycolor(color):
  if color=="red":
    print("\33[31m",sep="",end="")
  elif color=="white":
    print("\33[37m",sep="",end="")
  elif color=="blue":
    print("\33[34m",sep="",end="")
  elif color=="yellow":
    print("\33[33m",sep="",end="")






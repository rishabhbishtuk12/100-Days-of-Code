import random


def randomNumber():
    number = random.randint(1,90)
    return number

def prettyPrint():
  for row in my2DList:
    print(row)

my2DList = [[randomNumber(), 21, randomNumber()],
            [randomNumber(),"Bingo",randomNumber()],
            [randomNumber(), 17, randomNumber()]]

prettyPrint()



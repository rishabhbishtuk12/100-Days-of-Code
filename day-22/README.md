# Libraries
Libraries are collections of code that other people have written. Video games often use massive libraries (for example: game engines) to create the epic water reflections, 3-D graphics, etc.

We are going to start a bit smaller by just generating random numbers. (After all, random numbers are the basis of most games).

### Random library
We can use a library by writing "import" and then the library name.

This should always be one of the first lines of code.

👉 Let's import a library that will generate random numbers: (Does this look familiar from Day 14's Rock, Paper, Scissors game?)
```
import random
```
### How random works
In the code below, I have created a variable, 'myNumber'. I am making it equal to a random number given to me by the randint (random integer) library. I add the lowest number (1) and the highest number (100) that can be picked and the computer will generate a number at random.
```
import random
myNumber = random.randint(1,100)
print(myNumber)
```
# 👉 Day 22 Challenge

Copy and paste your code from Day 18.

We are going to make a change to this project:

Make the number generator completely random between 1 and 1,000,000. Now, the game will always have the user guess a random number each time (now the user can't cheat...)
``` 
Totally Random 0 to 4000
What is your guess?: 5
It's low
What is your guess?: 75
It's high
What is your guess?: 60
It's low
What is your guess?: 65
Correct!
It took you 4 guesses to get the number correct.
Click 'run' to try again with a different number.
```
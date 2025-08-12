# If Statements

These statements are a bit like asking a question. You are telling the computer: if something is true, then do this specific block of code. Double equals (==) is asking the computer to compare if these two things are exactly the same.  
In the code below, I am asking if the variable myName is the same as the string David.

```py
myName = input("What's your name?: ")
if myName == "David":
  print("Welcome Dude!")
```

## What is else?

If the condition is not met with the if statement, then we want the computer to do the else part instead. Likewise, if the condition is met in the if statement, then the else bit is ignored by the computer. The else statement must be the first thing unindented after the if statement and in line with it

```python
myName = input("What's your name?: ")
if myName == "David":
 print("Welcome Dude!")
 print("You're just the baldest dude I've ever seen")
else:
 print("Who on earth are you?!")
```

## Fix this code

```python
drink = input("Do you prefer coffee or tea?)
if drink = "coffee"
  print("Tea is better.")
    else:
  print("Excellent choice.")
```

Solution:

```py
drink = input("Do you prefer coffee or tea?")
if drink == "coffee":
  print("Tea is better.")
else:
  print("Excellent choice.")
```

## Challenge

1. Ask your users a series of questions that identify if they're one of the characters in the world you have created.
2. Add multiple if statements to check the result of each question.
3. Make sure to have a final print if they haven't selected any of the characters so far.

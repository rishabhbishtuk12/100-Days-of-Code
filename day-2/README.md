# Inputs and Variables

## Taking user input

```python
input("What's your name?: ")
# This will prompt the user to enter their name
```

## Variables

### What is a variable?

input asks for something, takes it, but then has nowhere to put it. We can change that with a variable which is a value that we can use to name and store data.

### Naming variables

You can give a variable any name you want, but you can't use spaces. You can use:

- underscores_between_words
- camelCaseToMakeItEasierToRead

```python
myName = input("What's you name? ")
myAge = input("How old are you? ")
print("Gee, that's REALLY OLD")
replit = input("Do you like Replit? ")
print("OF COURSE YOU DO!")
```

We now have three variables:

- myName has the user's name in it
- myAge is storing their age
- replit is storing their feelings about this amazing website.

## Printing a Variable

You can print your variable using print and the name you used for your variable in your input command.

```python
print()
print("So, you are")
print(myName)
print("and are the ripe old age of")
print(myAge)
print("and clearly think that Replit is")
print(replit)
print("That's great!")
```

## Fix my code

Try and fix this code which is full of errors.

```python
print("Definitely not a Phishing Scam")
print()
input("Your Name")
print("Thanks for logging in")
print(myName)
cardNumber = input("What is your credit card number?")
print("Thanks, I definitely wont put")
print("cardNumber")
print("into Amazon and order anything weird")
print()
print("Promise")
maidenName input("What is your Mother's maiden name? ")
print()
print("That's cool, I just wanted to know that")
print(maidenName)
print("was your Mum's maiden name. Not because the bank requested it or anything, honest.")
```

Solution:

```python
print("Definitely not a Phishing Scam")
print()
myName = input("What is your name?")
print("Thanks for logging in")
print(myName)
cardNumber = input("What is your credit card number?")
print("Thanks, I definitely won't put")
print(cardNumber)
print("into Amazon and order anything weird")
print()
print("Promise")
maidenName = input("What is your Mother's maiden name? ")
print()
print("That's cool, I just wanted to know that")
print(maidenName)
print("was your Mum's maiden name. Not because the bank requested it or anything, honest.")
```

## Challenge

1. Asks for the user's name, favorite food, favorite music and where they live (or you can create other questions!)
2. Store all of the answers in different variables.
3. Print out a full sentence that includes the user's favorite things.
4. Give them a positive affirmation at the end - tell them they rock at doing something!

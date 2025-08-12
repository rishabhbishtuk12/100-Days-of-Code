# Nesting

Nesting is where we put an if statement within an if statement using the power of indenting. The second if statement within the first if statement must be indented and its print statement needs to be indented one more time.

```python
tvShow = input("What is your favorite tv show? ")
if tvShow == "Game of Thrones":
  print("Ugh, why?")
  faveCharacter = input("Who is your favorite character? ")
  if faveCharacter == "Jon Snow":
    print("Right answer")
  else:
    print("Nah, Jon Snow's the greatest")
elif tvShow == "Breaking Bad":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")
```

## Fix the code

```python
order = input(What would you like to order: pizza or hamburger? ")
if order = "hamburger":
print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
  print("You got it.")
else:
    print("No cheese it is.")
elif order == pizza:
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings = "yes"
    print("We will add pepperoni.")
else:
  print"Your pizza will not have pepperoni.")
```

Solution:

```python
order = input("What would you like to order: pizza or hamburger? ")
if order == "hamburger":
  print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
    print("You got it.")
  else:
    print("No cheese it is.")
elif order == "pizza":
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings == "yes":
    print("We will add pepperoni.")
  else:
    print("Your pizza will not have pepperoni.")
```

## Challenge

### Fake Fan Question Generator

Wanna find out if someone else is a true superfan of the same show, movie or interest as you? Create a program that asks what someone is interested in and includes nested if statements to ask annoying follow-up questions to see if someone is the real deal!

Make sure you include multiple if/elif statements and nested if statements too!
    
# elif

The `elif` command (which stands for 'elseif') allows you to ask 2, 3, 4 or 142 questions using the same input! This command must be in a certain place. You can have as many `elif` statements as you want, but they must go in between `if` and `else` and have the same indentation. The `print` statements in your `elif` command need to line up with the indent of the other `print` statements.

```python
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "mark" and password == "password":
 print("Welcome Mark!")
elif username == "suzanne" and password == "Su74nne":
 print("Hey there Suzanne!")
else:
 print("Go away!")
```

## Fix this code

```python
season = input(what is your favorite season?)
if season = "spring"
  print("Ah! The birds are chirping and flowers blooming.")
  elif season == summer:
  print("Catch some sun and cool off with a lemonade.")
elif season == autumn
print("The leaves are changing and the air is crisp. Enjoy!)
      elif season = winter:
      print("Stay warm by the fire and watch the snow fall.")
else:
print("I don't know that season. Please try again.")
```

Solution:

```python
season = input("What is your favorite season?")
if season == "spring":
  print("Ah! The birds are chirping and flowers blooming.")
elif season == "summer":
  print("Catch some sun and cool off with a lemonade.")
elif season == "autumn":
  print("The leaves are changing and the air is crisp. Enjoy!")
elif season == "winter":
  print("Stay warm by the fire and watch the snow fall.")
else:
  print("I don't know that season. Please try again.")
```

## Challenge

1. Create a program where someone logins with their username and password correctly and then gets a lovely individual greeting.

2. Write a specific personalized greeting for 3 different people.
3. Don't forget an else statement for everyone else who shouldn't be logging in.

# 👉 Day 41 Challenge

Create a dictionary that stores the following information about a website: name, URL, description and a star rating (out of 5).
Use a loop to output the names of the keys, ask the user to type in the details and store the input in the dictionary.
Finally, output the whole dictionary (keys and values).
🥳 Extra points for getting all the inputs with just one input command and the split function.

Example:

```
🌟Website Rating🌟
Input the website name: Replit
Input the URL: replit.com
Input your a description: An awesome online IDE.
Input the a star rating out of 5: **\***
name:Replit, URL:replit.com, description:An awesome online IDE, rating:**\***
```

# Dictionaries With Loops

Loops and lists are a perfect pair. Dictionaries and loops are a bit trickier. This is because each dictionary item is made up of two parts - the name of the key and the actual value of that key.

## I've Lost My Keys!

Let's set up a looped dictionary.

👉 Using a `for` loop, like we would with a list, will output the values, but not the keys. Not ideal.

```py
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}
for i in myDictionary:
print(myDictionary[i])
```

👉 This loop uses the `.values()` method, which can be run on a data type. We still only get the value, and not the key.

```py
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}
for value in myDictionary.values():
print(value)
```

## I've Got The Key...I've Got The Secret

There is a better way!

Here's a loop that will output both key and value.

👉 The `.items()` function returns the key name and value. Note that I've supplied the loop with two arguments: 'name' and 'value').

This example will just output the names and values using an fString.

```py
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}
for name,value in myDictionary.items():
print(f"{name}:{value}")
```

## A Bit Iffy

Let's go one step further and use some `if` statements inside the loop.

👉 This example makes a comment about the strength key.

```py
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}
for name,value in myDictionary.items():
print(f"{name}:{value}")
if (name == "strength"):
print("Whoa, SO STRONG!")
```

👉This example uses nested `if` statements to react to the key name and the value stored within it.

```py
myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}
for name,value in myDictionary.items():
print(f"{name}:{value}")
if (name == "strength"):
if value > 100:
print("Whoa, SO STRONG")
else:
print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")
```

# 👉 Day 52 Challenge

There's no place like Rome...Or Napoli, Milan, possibly even New York if you must.

Just not the dodgy 2am 'round bread with suspicious toppings' merchants that I definitely do not visit on my way home from a night out.

That's right, you're opening a pizza shop! Try not to get anchovy on your keyboard. Man that stuff never washes out.

Regardless, your program today must:

1.  Prompt the user to input the quantity and size of pizzas.

2.  Multiply the two inputs together to calculate the cost of the pizzas.

3.  Store that in a 2D list with the user's name.

4.  Use `try.... except` for two reasons:

    - Include auto-save and auto-load. Use it with the auto-load.

    - When casting the quantity of pizzas to an integer. Avoid the user crashing the program by typing 'three' instead of '3'. Or any other non-integer input. If they do, then prompt them to try again.

Example:

```
🌟Dave's Dodgy Pizzas🌟
How many pizzas? > three
You must input a numerical character, try again. > 3
What size? > XXXXXX
Name please > David
Thanks David, your pizzas will cost XXXXX
```

# Avoiding Crashes

Sometimes, we just can't code around a crash. It's coming anyway, and all you can do is brace for impact.

Until now!

Let's look at an example based on yesterday's lesson.

👉 In this example, if the 'Stuff.mine' file doesn't exist, then the code will throw a 'no such file' error.

```py
myStuff = []
f.open("Stuff.mine","r")
myStuff = eval(f.read())
f.close()
for row in myStuff:
print(row)
```

## Try...except

The new construct to get around this is called `try.... except`

All the code that should work goes inside the `try`.

![alt text](image.png)

The error messages/instructions to handle any errors running the `try` code go inside the `except.`

![alt text](image-1.png)

👉 Like this:

```py
myStuff = []
try:
f.open("Stuff.mine","r")
myStuff = eval(f.read())
f.close()

# Try to find a file called 'Stuff.mine' and open it

except:
print("ERROR: Unable to load")

# If the file can't be found, show the error instead of crashing the whole program

for row in myStuff:
print(row)
```

## You are a Software Developer!

`try.... except` is great for improving the user experience to reduce frustration.

However, there are problems with just putting the whole code in a 'try except'.

As developers (yes you are a software developer now), it'd be nice to know what sort of error has occurred so that we have a better idea of how to fix it.

We can tell `except` what type of error(s) to look for. `Exception` (capital 'E') means 'every type'. I've captured the error type in the 'err' variable and printed it out to tell me what the error is. Here's a list of some built in `except` error codes.

![alt text](image-2.png)

👉 Look at how I've extended the `except` now.

```py
myStuff = []
try:
f.open("Stuff.mine","r")
myStuff = eval(f.read())
f.close()

# Try to find a file called 'Stuff.mine' and open it

except Exception as err:
print("ERROR: Unable to load")
print(err)

for row in myStuff:
print(row)
```

## Traceback

We could even get rid of the 'err' variable entirely and print a traceback, which will show you the red error tracing you see when python crashes.

I've created a 'debugMode' variable at the top of my code and pu the traceback in an `if` inside the `except`.

👉 This lets me show/hide the tracebacks easily by setting `debugMode` to True/False:

```py
debugMode = True
myStuff = []
try:
f.open("Stuff.mine","r")
myStuff = eval(f.read())
f.close()

# Try to find a file called 'Stuff.mine' and open it

except Exception:
print("ERROR: Unable to load")
if debugMode:
print(traceback)
for row in myStuff:
print(row)
```

![alt text](image-3.png)

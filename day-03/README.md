# Concatenate

```python
myName = input("What's your name? ")
myLunch = input("What are you having for lunch? ")
print(myName, "is going to be chowing down on", myLunch, "very soon!")
```

It turns out print has a super-power. We can give it as many different things to print as we want. All we need to do is put a comma , between every different thing in the ().

```python
number = input("Give me a number: ")
group = input("Give me a collective noun for a group of things: ")
thing = input("Give me the name of a weird or wacky thing: ")
print("No I don't think that", number, "is a", group, "of", thing,". That's just odd.")
```

## Fix the code

```python
print("=== Your Song Generator ===")
print("""You'll be asked a bunch of questions
then we'll make you up an amazing
song, totally copyright free 😭""")
print()
person = input("Name a person famous for something good: ")
thing = input("Name a thing they did: ")
place = input("Name a place you like: ")
rhyme = input("Give me a verb that rhymes with your person's name: ")
print()
print("There was a person called" name)
print("Who did something cool like", thing, "at the wonderful", place "where you'll find me", rhyme)
```

```python
print("=== Your Song Generator ===")
print("""You'll be asked a bunch of questions
then we'll make you up an amazing
song, totally copyright free 😭""")
print()

person = input("Name a person famous for something good: ")
thing = input("Name a thing they did: ")
place = input("Name a place you like: ")
rhyme = input("Give me a verb that rhymes with your person's name: ")

print()
print("There was a person called", person, "Who did something cool like", thing, "at the wonderful", place,  "where you'll find me", rhyme)
```

## Challenge

1. Create these as a variable:

   - A type of food
   - A type of plant
   - A method of cooking
   - A word to describe burned food
   - A household item

2. Output a nice looking Recipe page that _concatenates_ a dish in this format:

   - cooking food with burned plant on a bed of item

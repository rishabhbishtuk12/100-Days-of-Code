print("Marvel Movie Character Creator")
print("-----------------------------")

print("Answer these questions and let's find out.")
print()
print("Please use Y or N for yes and no.")

print()

isSpiderMan = input("Do you like 'hanging around'? ")
if isSpiderMan == "Y":
  print("Then you are Spider-Man!")
  exit()
else:
  print("Then you are not Spider-Man!")

print()

isIronMan = input("Do you think building robots is cool? ")
if isIronMan == "Y":
  print("Aha! You are Iron Man!")
  exit()
else:
  print("Then you are not Iron Man!")

print()

isHulk = input("Do you like smashing things? ")
if isHulk == "Y":
  print("You are Hulk!")
  exit()
else:
  print("Then you are not Hulk!")

print()

isThor = input("Do you like throwing things? ")
if isThor == "Y":
  print("You gotta be Thor!")
  exit()
else:
  print("I guess you are not like any of the Avengers!")

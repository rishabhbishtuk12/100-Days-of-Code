print("Are you a superfan of 'Game of Thrones' or a fake fan? ")
print()
print("Answer these questions to find out. (Use Capital Casing)")
print()
Dracarys = input(
    "What does Daenerys say when commanding her dragons to breathe fire? ")
if Dracarys == "Dracarys":
  print("Correct!")
  print()
  Needle = input("What is the name of Arya’s sword? ")
  if Needle == "Needle":
    print("Correct!")
    print()
    Braavos = input(
        "Where is the House of Black and White, the training temple of the Faceless Men? "
    )
    if Braavos == "Braavos":
      print("Correct!")
      print()
      Ghost = input("What is the name of Jon Snow's Direwolf? ")
      if Ghost == "Ghost":
        print("Correct!")
        print("Congratulations! You are a superfan!")
      else:
        print("Try again!")
        print("You are not a superfan!")
    else:
      print("Try again!")
      print("You are not a superfan!")
  else:
    print("Try again!")
    print("You are not a superfan!")
else:
  print("Wrong!")
  print("You are not a superfan!")

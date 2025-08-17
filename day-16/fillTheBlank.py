print (" Fill in the blank Lyrics !")
print("(type in the blank lyrics, see if you're as cool as me ")
tr = 0
while True :
  blank = input("\nNever going to ------- you up ")
  tr += 1
  if blank == "give":
    print("\nWell done, it only took ", tr," attepts !")
    break
  else :
    print("\nNope, try again. ")

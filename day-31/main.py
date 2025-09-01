def color(color):
  if color=="red":
    return ("\33[31m")
  elif color=="white":
    return ("\33[37m")
  elif color=="blue":
    return ("\33[34m")
  elif color=="yellow":
    return ("\33[33m")
  
title = f"{color('red')}={color('white')}={color('blue')}= {color('yellow')}Music App {color('blue')}={color('white')}={color('red')}="



print(f"             {title:^35}")

print(f"🔥▶️\t{color('white')}Radio Gaga")
print(f"\t{color('yellow')}Queen")

prev =f"PREV"
next =f"NEXT"
pause =f"PAUSE"

print(f"{color('white')}{prev:<20}")
print(f"{color('blue')}{next:^20}")
print(f"{color('red')}{next:>20}")
print()

title2 = f"WELCOME TO"
Armbook = "--  Armbook   --"
print(f"{color('white')}{title2:^35}")
print(f"{color('blue')}{Armbook:^35}")
line1 = "Definitely not a rip off of"
line2 = "a certain other social"
line3 = "networking site"
end = "Honest"
end2 = "Username:"
end3 = "password"

print(f"\n{color('yellow')}{line1:>35}")
print(f"{color('yellow')}{line2:>35}")
print(f"{color('yellow')}{line3:>35}")
print(f"\n{color('red')}{end:^35}")
text = "Username: "
username = input(f"\n{color('white')}{text:^35}")
text = "Password: "
username = input(f"{color('white')}{text:^35}")
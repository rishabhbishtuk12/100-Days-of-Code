birthYear = int(input("What year were you born? "))
if birthYear >= 1925 and birthYear <= 1947:
  print("You are a Traditionalist. 👴")
elif birthYear >= 1947 and birthYear <= 1964:
  print("You are a Baby Boomer! How you doing? 👶")
elif birthYear >= 1965 and birthYear <= 1981:
  print("You are a Generation X! What's up? 😎")
elif birthYear >= 1982 and birthYear <= 1995:
  print("You are Millenial! How you doin'? 😜")
elif birthYear >= 1996:
  print("You are Gen Z! What's trending? 🤩")
else:
  print("Try again! 🤔")
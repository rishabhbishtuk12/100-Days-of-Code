print("Secure Login")
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "John" and password == "CantSeeMe":
  print("Let's go John!")
elif username == "Jane" and password == "ILovePython":
  print("Welcome, Jane! you look amazing today.")
elif username == "Jesse" and password == "ScienceMagnets":
  print("Yo Jesse! What's up?")
else:
  print("Login failed. Try again.")

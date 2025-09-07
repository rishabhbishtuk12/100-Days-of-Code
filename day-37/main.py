
import time,os

heading ="\033[34mSTAR WARS NAME GENRATOR\n\033[0m"
print(f"{heading:^35}")
def clear(a):
  time.sleep(a)
  os.system("clear")
  print(f"{heading:^35}")
while True:
  

  firstName = input("Enter your first name: ")
  clear(1)
  lastName = input("Enter your last name: ")
  clear(1)
  mumMaiden = input("Enter your Mum's maiden name: ")
  clear(1)
  cityName = input("Enter the city where you were born: ")
  clear(1)
  starwarsName = (f"{firstName[0:3]}{lastName[0:2]} {mumMaiden[0:2]}{cityName[-3:]}").title()
  print(f"Your Star Wars name is Davha Mutol \033[34m {starwarsName}\033[0m")
  print()
  clear(4)
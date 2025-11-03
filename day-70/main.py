import os
from dotenv import load_dotenv
load_dotenv()

password = os.getenv('password')
print(password)
userPass = input("Password: ")
password = str(password)
if userPass == password:
    print("WELL COME")
else:
    print("Better luck next time")
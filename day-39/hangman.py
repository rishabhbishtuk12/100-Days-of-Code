import os,time
import random
from dotenv import load_dotenv
load_dotenv()
from google import genai
from google.genai import types

api_key = os.getenv("API_KEY_GOOGLE")
client = genai.Client(api_key=api_key)
head ="\033[31m Guess : HANGMAN \033[0m"
def selectShow():
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a agent. Your name is Hanger.User will provide you name of a series or a movie and your task is to give an string exact 10 one-word name of characters separate them with commas that series or movie. "),
        contents=ask
        
    )
    listOfName=response.text.split(",")
    # print(response.text)
    return listOfName
    # print(listOfName[0])
def hand():
    if hang == 6:
        print('''
_____________________
|          |        |
|                   |
|                   |
|                   |
|                   |
''')
    elif hang == 5:
        print('''
____________________
|          |       |      
|                  | 
|          |       |
|                  |
|                  |
''')
    elif hang == 4:
        print('''
____________________
|          |       |  
|                  | 
|        --|       |
|                  | 
|                  |
''')
    elif hang == 3:
        print('''
_____________________
|          |        |
|                   |         
|        --|--      | 
|                   | 
|                   |
''')
    elif hang == 2:
        print('''
_____________________
|          |        |
|                   |
|        --|--      |
|         /         |
|                   |
''')
    elif hang == 1:
        print('''
_______________________
|          |          | 
|                     |
|        --|--        |
|         / \         |
|                     |
''')
    elif hang == 0:
        print('''
_______________________
|          |          |
|         (^) - DEAD  |  
|        --|--        |
|         / \         |
|                     |
''')

hang = 6
# To ask from aI
print(f"{head:^40}")
hand()
ask=input("Select any Series or movie: ")

listOfWords=selectShow()
myWord = random.choice(listOfWords).lower()

print("\n",myWord)
letterPicked=[]
life=6


while life!=0:
    time.sleep(1)
    os.system("clear")
    print(f"{head:^40}")
    hand()
    letter=input("\nChoose a letter: ").lower()
    print()


    if letter in myWord:
        print("\nYou found a letter")
        letterPicked.append(letter)
    else:
        print("Nope, not in there")
        life-=1
        hang-=1
        print("\nOnly", life,"lives left")

    allLetter = True
    print()
    for i in myWord:
        if i in letterPicked:
            findWord=f"\033[32m{i}\033[0m"
            print(findWord, end="")
        else:
            print("_", end="")
            allLetter = False
    print()
    if allLetter:
        print(f"\nYou won with {life} left!")
        break
    elif life == 0:
        time.sleep(1)
        os.system("clear")
        hand()
        print(f"\nYou ran out of lives! The answer was {myWord}")

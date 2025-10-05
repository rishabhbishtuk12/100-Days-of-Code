import time,os

def palindrome(word):
    if len(word) <=1:
        return "is a palindrome. Yay!"
    if word[0] != word[-1]:
        return "is not a palindrome."
    return palindrome(word[1:-1])
    

while True:
    os.system("clear")
    print("🌟Palindrome Checker🌟")
    word = input("Input a word > ")
    print(word,palindrome(word))
    time.sleep(1)

    
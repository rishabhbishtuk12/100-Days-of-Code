import os,time

while True:
    os.system("clear")
    print("HIGH SCORE TABLE\n")
    f = open("HighScoreTable.txt","a+")
    initials = input("INITIALS > ")
    score = input("SCORE > ")
    f.write(F"{initials}    {score}\n")
    f.close()
    print()
    print("ADDED")
    time.sleep(1)
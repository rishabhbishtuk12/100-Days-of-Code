print('''
            Welcome to The Great Multiplication Challenge!
          --------------------------------------------------
🧠 Test your multiplication skills and see how many you can get right! 
''')
print()
print('''Game Rules:
1. 10 multiplication questions.
2. Each correct answer gives you 1 point.
4. Total score will be shown at the end out of 10.
''')

point=0
while True:
    start=input("Start the game : yes/no ")
    if start == "yes":
        choose=int(input("Name your multiples: "))
        for count in range(1,11):
            result=choose*count
            print(choose,"x",count,"=")
            ans=int(input(""))
            if ans == result :
                print("Great work! ")
                print()
                point+=1
            else:        
                print("Nope! The answer was",result)
                print()

        if point == 10:
            print("All correct?! You’re on fire! 🔥💯🙌")
            print("Math is not about numbers, it's about thinking! 🧠✨")
            break
        else:
            print("You score",point,"out of 10")
            print("Every expert was once a beginner.")
            break
    elif start == "no":
        print()
        print("Even the calculator’s feeling lonely now.😢")
        break

    else:
        print("wrong input")
        continue
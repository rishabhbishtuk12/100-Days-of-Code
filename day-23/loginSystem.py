def logIN():
    userNameInSystem = "rishabh"
    passwordInSystem = "123"
    while True:
        userName = input("What is your username: ")
        password = input("What is password: ")
    
        if userName == userNameInSystem and password == passwordInSystem :
            print("Welcome!!")
            break
        else:
            print("Whoops! I don't recognise that username or password. Try again ")
            print()
            continue

print("LOGIN SYSTEM")
logIN()




print(" E P I C  B A T T L E ")
while True:
    Player1 = input("P1 Select your move (r, p or s) ")

    if Player1 == "r" or Player1 == "p" or Player1 == "s" :
        while True:
            Player2 = input("P2 Select your move (r, p or s) ")
            if  Player2 == "r" or  Player2 == "p" or  Player2 == "s" :
                if (Player1 == "r") and (Player2 == "s"):
                    print("Player 1 Win")
                    break
                elif  (Player1 == "r" ) and (Player2 == "p"):
                    print("Player 2 Win")
                    break 
                elif  (Player1 == "p" ) and (Player2 == "s" ):
                    print("Player 2 Win")
                    break 
                elif  (Player1 == "p" ) and (Player2 == "r"):
                    print("Player 1 Win")
                    break 
                elif  (Player1 == "s" ) and (Player2 == "r" ):
                    print("Player 2 Win")
                    break 
                elif  (Player1 == "s" ) and (Player2 == "p" ):
                    print("Player 1 Win")
                    break 
                else :
                    print("It's a Tie")
                    break
            else :
                print("wrong input")
                continue
    else :
        print("wrong input")
        continue
    ask = input("You want to play again ")
    if ask == "yes":
        continue
    else :
        print("Game Over")
        break
        
print(" Exam Grade Calculator ")
subName = input("Name of Exam : ")
maxNumber = float(input("Max. Possible Score : "))
youScore = float(input ("Your Score : "))

num = (youScore / maxNumber) * 100

if (num >= 90):
  print(" You got ", num ,"Which is a" "\033[32m" " A+ ")
elif (num >= 80 and num < 90 ):
   print(" You got ", num ,"Which is a" "\033[32m" " A ")
elif (num >= 70 and num < 80 ):
 print(" You got ", num ,"Which is a" "\033[34m" " B ") 
elif (num >= 60 and num < 70 ):
 print(" You got ", num ,"Which is a" "\033[34m" " C ")
elif (num >= 50 and num < 60 ):
 print(" You got ", num ,"Which is a" "\033[33m" " D ") 
elif (num >= 40 and num < 50 ):
 print(" You got ", num ,"Which is a" "\033[33m" " U ") 
else :
  print(" You got ", num ,"Which is a" "\033[31m" " F ") 
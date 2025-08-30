# for i in range(0, 10):
#     print(i,end=" ")

# print("If you put", "\33[33m"," nothing as the", "\33[35m", " end character", "\33[32m", " then you don\"t", "\33[33m"," get odd gaps", sep="")

# import os, time

# print('\033[?25l', end="")

# for i in range(1,101):
#     print(i)
#     time.sleep(0.01)
#     os.system('clear')

# print('\33[?35h', end="")

def colorText(text):
    
    print(text, end="\33[0m")
 

print("Super Subroutine")
print("\n With my", end="\33[35m")
colorText(" new program")
print("I can just call red(""and"")", end="\33[91m")
colorText(" and")
print(" that word will appear in the color I set it to.")
print("\n With no", end="\33[94m")
colorText(" weird gaps.")
print("\n \n Epic.")
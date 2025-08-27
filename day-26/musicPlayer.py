import os
import time
import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()
def pause():
    pygame.mixer.pause()

pause()
def play():
    pygame.mixer.unpause()
    while True:
        stopInput=(int(input("Press 2 anything to pause or see the menu")))
        if stopInput== 2:
            pause()
            return
        else:
            continue

while True:
    os.system("clear")
    print("MyPOD music player")
    time.sleep(2)
    print("Press 1 for play")
    print("Press 2 for Pause")
    print()
    print("Press anything else to see the menu again.")
    userInput=int(input())
    if userInput==1:
       print("Playing some proper tunes!")
       play()
    elif userInput==2:
        pause()
    else:
        continue    
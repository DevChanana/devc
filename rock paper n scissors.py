import random
import time

r_p_s = ["ROCK","PAPER","SCISSORS"]

for i in range(12):
    print("Round", i + 1)

    you = input("Write BETWEEN ROCK PAPER AND SCISSOR: ")

    computer = random.choice(r_p_s)
    time.sleep(2)
    print("Rock")
    time.sleep(2)
    print("Paper")
    time.sleep(2)
    print("Scissor")
    time.sleep
    print("COMPUTER CHOOSE" ,computer)
    time.sleep(2)
    if(computer == you):
        print("Its A Draw")
    elif(computer == "ROCK" and you == "PAPER"):
         print("YOU WIN")
    elif(computer == "PAPER" and you == "SCISSOR"):
         print("YOu WON")
    elif(computer == "SCISSOR" and you == "ROCK"):
         print("YOUN WON")
    else:
        print("You lost")
        break


# update log (2/12/26):
# LOGIC ERRORS:
#     Fixed logic issue with AI
# GENERAL
#     Better AI
#     Cleaner code
#______________CODE______________#
#_____________IMPORTS_____________#
from random import randint
import time
#______________MAIN______________#
def main():
    while True:
        phand = randint(2, 21)
        dhand = randint(2, 21)
        while True:
            print(f"Your hand is {phand}")
            drawYN = str(input("1 to draw, 2 to stay --->"))
            if drawYN == str(1):
                phand = phand + randint(1, 11)
                if phand > 21:
                    print(f"Your hand is {phand}")
                    print("You Lose!")
                    pgain = int(input("Play Again (1/2)?"))
                    if pgain == 1:
                        break
                    else:
                        quit()
            elif drawYN == str(2):
                while dhand < 16 and dhand < phand:
                    print(f"The dealer's hand is {dhand}")
                    time.sleep(.5)
                    dhand += randint(1, 11)
                if dhand == phand:
                    print(f"YOU BREAK EVEN! HOUSE: {dhand}")
                    pgain = int(input("Play Again (1/2)?"))
                    if pgain == 1:
                        break
                    else:
                        quit()
                elif dhand < phand:
                    print(f"YOU WIN! HOUSE: {dhand}")
                    pgain = int(input("Play Again (1/2)?"))
                    if pgain == 1:
                        break
                    else:
                        quit()
                elif phand < dhand:
                    print(f"YOU LOSE! HOUSE: {dhand}")
                    pgain = int(input("Play Again (1/2)?"))
                    if pgain == 1:
                        break
                    else:
                        quit()
            else:
                print("NOT AN OPTION")
#_____________MAIN_2_____________#
input("WELCOME TO BJv3! PRESS ENTER TO PLAY!")
if __name__ == '__main__':
    main()
#____________FINISHED____________#





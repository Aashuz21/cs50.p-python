import random
import time

while True:
    guess=input("Heads or Tails:").capitalize()
    if guess not in["Heads","Tails"]:
        print(f"Mf!! You are here for coin toss;not for {guess} doing")
    else:
        print ("Flipping the Coin.......(Hold for 2 seconds)")
        time.sleep(2)
        coin=random.choice(["Heads","Tails"])
        if coin == guess:
            print("You won")
        else:
            print("Better luck next time")

        play=input("Do you want to play again? y/n:").lower()
        if (play=="y"):
            continue
        else:
            break


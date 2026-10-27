import random
def onlypositive(prompt):
    while True:
        try:
            n=int(input(prompt))
            if n<0:
                raise ValueError ("Not a positive number")
            else:
                return n
        except ValueError as e:
            print(f"{e}")

n=onlypositive("Level:")
secret=random.randint(1,n)
while True:
    guess=onlypositive("Guess")
    if guess==secret:
        print("Sakdaina ni feriii")
        break
    elif guess<secret:
        print("Too small ")
        continue
    else:
        print("Big as d..")
        continue
        
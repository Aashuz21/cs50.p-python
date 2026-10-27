import random
def main():
    n=get_level()
    i=1
    score=0
    while (i<=10):
        x=generate_integer(n)
        y=generate_integer(n)
        sum=x+y
        attempts=0
        while attempts<3:
            value=int(input(f"{x} + {y}:"))
            if value==sum:
                score=score+1
                break
            else:
                print("EEE")
                attempts=attempts+1
                if attempts==3:
                    print(f"{x}+{y}={sum}")
        i=i+1
    print(f"Score:{score}")
def get_level():
    while True:
        try:
            lvl=int(input("Level:"))
            if lvl not in [1,2,3]:
                raise ValueError("Level can be either 1 2 or 3")
            else:
                return lvl
        except ValueError as e:
            print(f"{e}")
            continue
        else:
            break

def generate_integer(level):
    if level==1:
       return random.randint(0,9)
    elif level==2:
        return random.randint(10,99)
    elif level ==3:
        return random.randint(100,999)

if __name__ == "__main__":
    main()


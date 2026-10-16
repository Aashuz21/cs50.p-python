def main():
    p=get_fraction()
    print(f"Percentage:{p}%")


def get_fraction():
    while True:
        try:
            fuel=(input("Enter the fractional part, x/y format:"))
            x_str,y_str=fuel.split("/")
            x=int(x_str)
            y=int(y_str)
            if x>y or y==0:
                raise ValueError
            else:
                percent=round((x/y)*100)
                return percent

        except(ValueError,ZeroDivisionError):
            pass

main()



def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    rm=float(d.replace("$",""))
    return rm


def percent_to_float(p):
    rm1=float(p.replace("%",""))/100
    return rm1


main()
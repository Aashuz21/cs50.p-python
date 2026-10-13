#Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

#In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

due=50
while due > 0:
    print(f"Amount Due:{due}")
    try:
        amt=int(input("Insert coin:"))
        if amt==25 or amt==10 or amt==5:
            due=due-amt
        else:
            raise ValueError("We only accept 25,10 or 5 cent coin")
    except ValueError as e :
        print(f"Invalid input:{e}")
        print("Please try again")
change_owed=abs(due)
print(f"Change Owed:{change_owed}")



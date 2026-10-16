menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total=0
while True:
    try:
        order=input("Enter the name of dish you want:").title().strip()
        if not (order in menu):
            print("Not in the list")

        else:
            total=total+menu[order]
            print(f"Total:${total}")

    except EOFError:
        break

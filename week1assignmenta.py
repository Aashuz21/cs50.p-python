deep=input("What's the answet to the great question of life , the universe and everything?")
if deep=="42" or deep=="forty-two" or deep=="forty two":
    print("yes")
else:
    print("no")


# classical textbook error can rise here; when you are asking for the value from the user; you will most likely ask in string; now if you only write deep= 42; but the computer has saved it as "42" so the problem can arise there; thats why ; i have used double quotation around 42; while representing; 
database={}
name=input("Enter the name of customerr:")
if name in database:
    print(f"Welcome Back, {name}")

else:
    print(f"New customer detected!! Creating an account for {name}")
    database[name]={"balance":0 ,"items":{}}

while True:
    try :
        item=input("Enter the name of item :")
        price=int(input(f"Enter the price for {item}"))
        database[name]["items"][item]=price
        database[name]["balance"]+= price 
    except EOFError:
        print("Thankyou for buying:")
        break

print(f"Total Udharo for {name} is Rs {database[name]['balance']}")
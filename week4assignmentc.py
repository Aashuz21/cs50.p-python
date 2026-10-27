import inflect
p=inflect.engine()
nas=[]
while True:
    try:
        name=input("Name:")
        nas.append(name)
    except EOFError:
        break
output=p.join(nas,conj="and")  # also if you want to remove the comma before the  and conjunction ; you can use final sep="";by telling this;; you tell the library dont out any separating character at last;
print(f"Adieu, adieu, to {output}")


# if you want to import the specific class you can do like this:
#from inflect import engine;
#p=engine()  // you still need to call the class for object creation;
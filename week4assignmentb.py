import pyfiglet
import random
import sys
f=pyfiglet.Figlet()  # pyfiglet is a module; and Figlet is a class inside that module; to access this class figlet we need an object;; without object we cant;; but we have seen some sort of thing called as static in .net  so if we normally use static;; we dont need an object at all ; we can just access the member of the class using the name of the class; 
fonts=f.getFonts()   # now using that f we accessed the member function getfonts() of that class; 
if len(sys.argv)==1:
    print("No arguments given, will use random font")
    chosen_font=random.choice(fonts)
elif len(sys.argv)==3:
    print("two arguments are given")
    if sys.argv[1] not in ["-f","--font"]:
        sys.exit("Invalid")
    if sys.argv[2] not in fonts:
        sys.exit("Motherfucker you here to joke??")
    chosen_font=sys.argv[2]
else:
    sys.exit("Invalid usage")
f.setFont(font=chosen_font)     #font inside the set font is the name of parameter; not fonts; because its your variable here .setfont() is also a member function of the class; so we accessed it using the object of that class; 
text=input("Give some text:")
print(f.renderText(text))  # render text is also a function here which takes an string an convert it into ascii art using whatever font was set. 


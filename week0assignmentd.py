c=300000000
def main():
       m=int(input("Enter the values of mass:"))
       print("The value of energy is :",calc(m))

def calc(m):
       E= m*pow(c,2)
       return E


main()
n=int(input("Enter number :"))
if(n%2==0):
    if(n>=2 and n<=5):
        print("N is not weird")
    elif(n>=6 and n<=20):
        print("weird")
    elif(n>20):
        print("Not weird")
else:
    print("N is weird")

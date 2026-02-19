user ="EMC"
password ="Diya1234"
count=0
def valid(user,password):
    return user ==user and password ==password
for Loop in range(3):
    a=input("Enter username : ")
    b=input("Enter Password : ")
    Result=valid(a,b)
    count=count+1
    if Result==True:
       print("Login Successfully")
       break
    else:
       print("Invalid data try again !!")
if count==3:
    print(f"The {count} attempt completed")


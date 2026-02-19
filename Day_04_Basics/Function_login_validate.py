#def valid(a,b):
    #if a=="EMC" and b=="123":
       # return True
    #else:
     #return False
#n=input("Enter user name: ")
#m=input("Enter Password: ")
#Result=valid(n,m)
#print(Result)
def valid(username, password):
    return username == "EMC" and password == "123"

n=input("Enter username: ")
m=input("Enter Password: ")
Result=valid(n,m)
print(Result)
    
    

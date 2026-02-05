ecount=0
ocount=0
for i in range(1,11):
    if(i%2==0):
        ecount=ecount+1
    elif(i%2==1):
        ocount=ocount+1
print("Even num count : ",ecount)
print("Odd num count : ",ocount)

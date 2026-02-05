print("Enter 3 Numbers")
a=[]
for i in range(1,4):
    num=int(input("Enter the number " + str(i)))
    a.append(num)
#print(a)
sum=0
count=0
for sa in a:
    count=count+1
    sum=sum+sa
print(sum)
print(sum/count)

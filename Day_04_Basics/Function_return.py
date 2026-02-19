def add(a,b):
    return a+b
n=int(input("Enter the number : "))
m=int(input("Enter the number : "))
result=add(n,m)
print(result)

#4️⃣ Difference: print vs return (Common Question)

#❌ Using print

#def add(a,b):
   # print(a+b)

#x = add(5,2)
#print(x)


#Output:

#7
#None


#Because function didn't return anything.

#✔ Using return

#def add(a,b):
    #return a+b

#x = add(5,2)
#print(x)


#Output:

#7

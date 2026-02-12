num1=int(input("Enter number : "))
num2=int(input("Enter number : "))
num3=int(input("Enter number : "))
if(num1<num2):
    if(num2<num3):
        print(f"The large number is1 {num3}")
    else:
        print(f"The large number is2 {num2}")
elif(num1>num2):
    if(num1<num3):
        print(f"The large number is3 {num3}")
    else:
        print(f"The large number is4 {num1}")
else:
    print(f"All the entered numbers are equal {num1}")


  

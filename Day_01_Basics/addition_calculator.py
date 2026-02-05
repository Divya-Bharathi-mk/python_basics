# Program : Intractive addition calculator
num1 = input("Enter first number:") # Taking input from user
num2 = input("Enter second number:") # Taking input from user
# Adding two numbers
sum = int(num1) + int(num2) # Converting string input to integer and adding, the data type conversion is need because input returns string by default.
# Display the sum
print(f"The total sum is: {sum}")

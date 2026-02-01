# Program 3: Voting Eligibility
# Concept: If-Else Statements and Comparison Operators
# 1. Get user input and convert to integer immediately
Age = int(input("Enter your age: "))
if Age >=18:
    print("Your eligible to vote")
else:
    print("Your not eligible to vote")
    print("Years remaining:", 18 - Age)
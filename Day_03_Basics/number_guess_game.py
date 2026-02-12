count=0
a=int(input("Guess the Secreat number : "))
while a!=7:
    print("Wrong guess, try again!")
    a=int(input("Guess the Secreat number : "))
    count=count+1
print(f"Correct! You guessed in {count+1} attempts")
        
    
  

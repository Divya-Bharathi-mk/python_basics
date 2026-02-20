class Rectangle:
     def __init__(self, length, width):
        self.length=length
        self.width=width
        
     def area(self):
        return self.length * self.width
    
     def perimeter(self):
        return 2*(self.length + self.width)
    
obj1=Rectangle(5,10)

#Area=obj1.area()
#Perimeter=obj1.perimeter()

print("The area: ",obj1.area())
print("The Perimeter: ",obj1.perimeter())


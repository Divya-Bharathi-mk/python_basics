class Mobile:
    def __init__(self, brand, price, ram):
        self.brand=brand
        self.price=price
        self.ram=ram
    def display(self):
        print("Brand: ",self.brand)
        print("Price: ",self.price)
        print("Ram: ",self.ram)
        print("-" * 20)

obj1=Mobile("Samsung",20000,"8GB")
obj2=Mobile("Apple",80000,"6GB")
obj3=Mobile("Oneplus",30000,"12GB")

obj1.display()
obj2.display()
obj3.display()

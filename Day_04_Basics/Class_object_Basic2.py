class goa():
    name=""
    drink=""
    def party(self):
        print("Lets party")
    def beach(self):
        print("Lets enjoy beach")
        
obj1=goa()
obj2=goa()

obj1.name="ramesh"
obj2.name="suresh"

obj1.drink="Yes"
obj2.drink="No"

print(obj1.name)
print("drink",obj1.drink)
print(obj2.name)
print("drink",obj2.drink)

ramesh.party()
suresh.beach()

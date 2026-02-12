#Dictionary {}
# Do not allow Duplciate but the duplcaite value will be overwrite with existing value
# Any type of data can be stored
# key:value pair {"name":"EMC"}
# get(), keys(), values(), items(), update({"Year":2020}),
# thisdict{"color"} = "red", thisdict.pop("module"), del, clear()
A={"name":"Divya","age":1,"students":["kavin","kannan","Divya","Sathish"]}
print(A)
print(A.keys())
print(A.values())
A["age"]=26
print(A.values())
A["Gender"]=["Male","Female"] #list added in the dictionary
A["Colors"]="Pink" # value added in the dictionary
A.update({"age":55}) #updated age value
print(A)
A.pop("age")#key:value will be removed
print(A)
del A["name"] # mentioned name deleted in the dictionary
print(A)
A.clear() # used to empty the dictionary values so it will remains {} only
print(A)
del A # over all A dictionary got deleted
print(A)

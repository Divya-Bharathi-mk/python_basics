# set {}
# Set not allowing Duplciate, if duplicate is there then it will be removed
# Any type of data can be stored
# We can not modify the data, but we can able to add or remove the data.
# sets are unordered (result will not be in ordered list same as set defined value order)
# add(), update(), remove(), pop()

A={1,2,3,4,5,6,7,1,2}
A.add(10)
A.remove(1)
A.update({1})
A.discard(22) 

#Both remove elements from set:

#remove() → throws error if element not present

#discard() → does nothing if element not present (safe)

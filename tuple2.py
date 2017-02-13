#tuples are read only lists
tuple = (25, 'abc', 20.1, "hi hello")
list = [30, 'xyz', "sushant"]

print (tuple)
print (list)

list[1]= 25
print (list)

tuple[1]= 50  #invalid syntax
print (tuple)
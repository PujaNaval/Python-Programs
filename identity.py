a = 10
b = 10

print('a =',a,':',id(a))
print ('b =',b,':',id(b))

if (a is b):
    print("a and b have same identity")

else:
    print("a and b do not have same identity")

if (id(a) == id(b)):
    print("a and b have same identity")

else:
    print("a and b do not have same identity")

b=30

if (a is not b):
    print("a and b do not have same identity")

else:
    print("a and b have same identity")



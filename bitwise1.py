
a=10
b=20

print ('a=',a,':',bin(a))
print ('b=',b,':',bin(b))

c=0

c = a & b
print ("Result of AND is", c, ':',bin(c))

c = a | b
print ("Result of OR is", c, ':',bin(c))

c = a ^ b
print ("Result of EXOR is", c, ':',bin(c))

c = ~a 
print ("Result of NEGATION OF a", c, ':',bin(c))

c = a <<2
print ("Result of LEFT SHIFT is", c, ':',bin(c))

c = a >>2
print ("Result of RIGHT SHIFT is", c, ':',bin(c))
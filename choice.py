
import random

n = random.choice(range(100))       #Random number from range

print('random number is:',n)

list = [1,2,3,4,5,6,8,9,0]         #Random number from list

l = random.choice(list)

print("Random number from list is: ",l)

s = "Python by Sushant"           #Random number from string
b = random.choice(s)
print("Random character: ",b)
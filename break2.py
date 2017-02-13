
n = int(input("Enter any number:"))

number = [10,11,12,13,15,16,17,18]

for a in number:
    if a == n:
        print ("Number found in list")
        break

else:
    print ("Number not found in list")

a = int(input("Enter Salary"))
ch =(input("Enter Gender"))

print ("Salary=",a)
print ("Gender=",ch)

if (ch == 'm'):
    if(a<10000):
       print("No Income Tax")

    else:
        it = a*.10
        print("Income Tax is:",it)

else:
    if(a<15000):
       print("No Income Tax")

    else:
        it = a* .10
        print("Income Tax is:",it)

print("Total Payable amount:",a+it)


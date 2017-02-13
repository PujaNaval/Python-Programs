
str = (input('Enter string'))
print (str)

cap = str.capitalize()      #first letter of string is capital
print (cap)

cen = str.center(10,'H')   #total width of the string and fill character
print (cen)

l = len(str)
print ("Length of string is %d"%(l))     #find length of the string

c = str.count('s',0,l)      #counts how many times character occurs
print ("Count is:",c)

str = "Hello123"            
print (str.isalnum())           #checks if number in string

str = "1234"
print (str.isdigit())              #checks string contains only digits

str = "   "                   #checks blank spaces in string
print (str.isspace())

str = "SUSHANT"              #converts upper to lower
print (str.lower())

str = "sushant"            #converts lower to upper
print (str.upper())

str = "sushant"                #find maximum character in string (ASCII)
print ('Maximum:',max(str))

str = "sushant"
print ('Maximum:',min(str))      #find maximum character in string (ASCII)
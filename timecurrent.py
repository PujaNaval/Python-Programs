
import time

ticks = time.time()                #getting ticks since 1 Jan 1970
print ('Total ticks:',ticks)

lt = time.localtime(time.time())   #getting current time

print ("Local current time: ",lt)

ft = time.asctime(time.localtime(time.time()))    #getting formatted time

print ("Formated current time:",ft)
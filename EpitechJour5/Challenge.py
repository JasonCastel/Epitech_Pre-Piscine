import random
import time
startingTime=time.time()

list=[]

for i in range(0,1000000):
    n = random.randint(1,1000000)
    list.append(n)
list.sort()
#print(list)

duration = time.time()-startingTime
print(duration)



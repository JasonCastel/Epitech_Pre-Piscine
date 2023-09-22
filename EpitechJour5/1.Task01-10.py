list =[1,2,3,4,5]
list2=[]
print(list[0])           #Task01
print(list[len(list)-1]) #Task02
list.append(6)           #Task03
print(list)              #Task04
list.remove(list[len(list)-1])    #Task05
print(list)

list.insert(0,0)         #Task06
print(list)

for i in range(1,6):     #Task07
    print(list[i])

list2 = list[::-1]       #Task08
print(list2)

print(list[0],list2[0])  #Task09

for b in range(0,17):    #Task10
    list.insert(list[len(list)-1],i)
print(list)







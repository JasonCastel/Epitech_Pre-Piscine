def bread () :
  print (" <////////// > ")
def lettuce () :
  print (" ~~~~~~~~~~~~ ")
def tomato () :
  print (" O O O O O O")
def ham () :
  print (" ============ ")
def nbr(x) :
  if x >= 0:
    return(x)
  else:
    print("Ce n'est pas possible")
def choix(y) :
  if y == "vege":
     y=0
     return(y)
  else:
     y=1
     return(y)
     

  

cpt1= int(input())
cpt2= input()



nbr(cpt1)
a=choix(cpt2)

if a == 1:

 for i in range(0,cpt1):
  bread()
  lettuce()
  tomato()
  ham()
  ham()
  bread()
else:
  for i in range(0,cpt1):
    bread()
    lettuce()
    lettuce()
    tomato()
    tomato()
    bread()


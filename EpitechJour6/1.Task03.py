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

cpt2= int(input())



nbr(cpt2)

for i in range(0,cpt2):
  bread()
  lettuce()
  tomato()
  ham()
  ham()
  bread()
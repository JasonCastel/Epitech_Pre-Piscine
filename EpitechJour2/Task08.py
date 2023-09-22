c=0
i=1

while c < 3.141590:
  c = abs(c - 4/i)
  i = i + 2
  c =   abs(c + 4/i)
  i = i + 2
  c = round(c,6)
  print(c)
print(c)
print(i)

 




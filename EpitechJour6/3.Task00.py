def funA(s,n):
    if n <= sum([int(c.islower()) for c in s]):
        print("Il y a plus de minuscule que le nombre entré")
    else:
        print("Il y a moins de minuscule que le nombre entré")    

    
def funB(s,n):
    if n <= sum([int(c.isupper()) for c in s]):
        print("Il y a plus de majuscule que le nombre entré")
    else:
        print("Il y a moins de majuscule que le nombre entré")

def funC(s,n):
    if n <= sum([int(c.isalpha()) for c in s]):
        print("Il y a plus de charactère que le nombre entré")
    else:
        print("Il y a moins de charactère que le nombre entré")
def funD(s,n):
    special=0
    for i in range(len(s)):
     if(s[i].isalpha()):
        continue
     elif(s[i].isdigit()):
        continue
     else:
        special = special + 1
    if n <= special:
        print("Il y a plus de caractère spécial que le nombre indiqué")
    else:
        print("Il y a moins de caractère spécial que le nombre indiqué")

def funE(s,n):
    if n <= sum([int(c.isdigit()) for c in s]):
        print("Il y a plus de nombre dans le string que le nombre entré")
    else:
        print("Il y a moins de nombre dans le string que le nombre entré")

funA("saluT",5)
funB("SaluT",3)
funC("salut45",3)
funD("S&l%t",2)
funE("s41u7",2)

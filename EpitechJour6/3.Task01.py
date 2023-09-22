def funA(s,n):
    if n<0:
        print("Veuillez entrez un nombre supérieur ou égal à 0")
    else:

      if n <= sum([int(c.islower()) for c in s]):
        print("bonjour")
        return True
      else:
        return False

    
def funB(s,n):
     if n<0:
        print("Veuillez entrez un nombre supérieur ou égal à 0")
     else:
      if n <= sum([int(c.isupper()) for c in s]):
        return True
      else:
        return False

def funC(s,n):
     if n<0:
        print("Veuillez entrez un nombre supérieur ou égal à 0")
     else:
      if n <= sum([int(c.isalpha()) for c in s]):
         return True
      else:
         return False
    
def funD(s,n):
    special=0
    if n<0:
        print("Veuillez entrez un nombre supérieur ou égal à 0")
    else:
     for i in range(len(s)):
      if(s[i].isalpha()):
        continue
      elif(s[i].isdigit()):
        continue
      else:
        special = special + 1
     if n <= special:
        print("Hello")
        return True
     else:
        return False

def funE(s,n):
     if n<0:
        print("Veuillez entrez un nombre supérieur ou égal à 0")
     else:
      if n <= sum([int(c.isdigit()) for c in s]):
        return True
      else:
        return False

def check_password(choix,s,n):
    A=''
    B=''
    C=''
    D=''
    E=''
    if choix == "lower":
        return funA(s,n)
    elif choix == "upper":
        return funB(s,n)
    elif choix == "char":
        return funC(s,n)
    elif choix == "special":
        return funD(s,n)
    elif choix == "number":
        return funE(s,n)


try:


 string=input("Choisissez un mot de passe: ")
 

 if check_password("lower",string,1) and check_password("special",string,1) and check_password("upper",string,1) and check_password("number",string,1):
    print("Le mot de passe est sécurisé")
 else:
    print("REFAIT LE MOT DE PASSE")
except(Exception)as error:
   print(error)
    






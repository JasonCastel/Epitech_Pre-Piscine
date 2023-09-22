import random

#pendu =["tic","coq","dock","dame","aimer","gifle","whisky","hurler","mondial","poterie","question","tabouret","klaxonner","mascarade","printemps","coquelicot","subjective","sorcellerie","zygomatique"]

def mot_fichier(nomFichier):
    with open(nomFichier,'r') as fichier:
        liste = [ligne.strip() for ligne in fichier]
        return liste

def jeux(s):
    result=['_'] * len(s) 
    guesses = set()
    faute = 0

    print("Jouons: ")
    essai = len(s) + 20

    while essai > 0:
        print(" ".join(result),"/",faute,"faute")
        lettre = input("Entrez une lettre: ")

        if lettre in guesses:
            print("Vous avez déjà deviner ",lettre)
            continue

        guesses.add(lettre)

        if lettre in s:
            print("Lettre trouvé")
            for i in range(len(s)):
              if s[i] == lettre:
                 result[i] = lettre   

            if "_" not in result:
                print(f"Bravo vous avez trouvé le mot {''.join(result)}","avec",faute,"fautes")
                break
        else:
            print("Mauvaise lettre")
            essai -=1
            faute +=1

        print("Il vous reste:",essai,"essai")

    if "_" in result:
        print("Vous avez perdu. Le mot était: ", s)

mottrouver=mot_fichier(r"C:\Users\jason\python\EpitechJour7\ods4.txt")
rand = random.randint(0, len(mottrouver) - 1)
metrouve = mottrouver[rand].lower()
jeux(metrouve)
 




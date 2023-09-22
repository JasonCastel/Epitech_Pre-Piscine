import random
import datetime

#pendu =["tic","coq","dock","dame","aimer","gifle","whisky","hurler","mondial","poterie","question","tabouret","klaxonner","mascarade","printemps","coquelicot","subjective","sorcellerie","zygomatique"]

def mot_fichier(nomFichier):
    with open(nomFichier,'r') as fichier:
        liste = [ligne.strip() for ligne in fichier]
        return liste

def jeux(s):
    result=['_'] * len(s) 
    guesses = set()
    score = 0

    print("Jouons: ")
    essai = len(s) + 20

    while essai > 0:
        print(" ".join(result))
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
                print(f"Bravo vous avez trouvé le mot {''.join(result)}","en",score,"essais")
                return score
        else:
            print("Mauvaise lettre")
            score +=1


    if "_" in result:
        print("Vous avez perdu. Le mot était: ", s)



def read_old_score(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            if content.startswith("Le meilleur score est:"):
                score_part = content.split(":")[1].split("(")[0].strip()
                if score_part.isdigit():
                    return int(score_part)
            return None
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Une erreur pendant la lecture du fichier: {e}")
        return None
    

mottrouver=mot_fichier(r"C:\Users\jason\python\EpitechJour9\ods4.txt")
rand = random.randint(0, len(mottrouver) - 1)
metrouve = mottrouver[rand].lower()


file_path =r"C:\Users\jason\python\test.txt"
old_score = read_old_score(file_path)
a = jeux(metrouve)

if old_score is None or a < old_score:
    with open(file_path, 'w') as file:
        new_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Le meilleur score est: {a} (mise à jour le {new_date})")
        print(f"Nouveaux meilleur score: {a}")
else:
    print(f"L'ancien meilleur score {old_score} est meilleur que votre score {a}. File not updated.")

 




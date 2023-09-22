Mot1 = "Cat"
Mot2 = "Garden"
Mot3 = "Mice"
Phrase = "thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"

envr=Phrase[::-1]

cpt1=Phrase.lower().count(Mot1.lower())
cpt2=Phrase.lower().count(Mot2.lower())
cpt3=Phrase.lower().count(Mot3.lower())

envr1=envr.lower().count(Mot1.lower())
envr2=envr.lower().count(Mot2.lower())
envr3=envr.lower().count(Mot3.lower())

result= cpt1 + cpt2 + cpt3 + envr1 + envr2 + envr3

print(result)
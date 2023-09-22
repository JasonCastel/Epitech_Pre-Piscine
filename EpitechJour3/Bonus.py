phrase = "Bonjour1a1tous21je1suis1Albert1Nestor21le1castor31En1janvier1de1l4année1dernière21plus1de1dix5mille1personnes1m4ont1voués1un1culte31C4était1marrant21mais1un1peu1bizarre31En1tout1cas1plus1que1de1s4appeler1Albert1Nestor1en1étant1un1castor."
mot1="castor"
new_phrase= phrase.replace("1"," ")
new_phrase2= new_phrase.replace("2",",")
new_phrase3= new_phrase2.replace("3",".")
new_phrase4= new_phrase3.replace("4","'")
new_phrase5= new_phrase4.replace("5","-")

cpt1=new_phrase5.lower().count(mot1.lower())
result= new_phrase5.replace("castor","Castor")



print(new_phrase5)
print(cpt1)
print(result)








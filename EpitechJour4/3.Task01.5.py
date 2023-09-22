MessageCrypte=input("Entrez un message à déchiffrer: ")
cle=int(input("Entrez la clé caesar: "))
lg=len(MessageCrypte)
MessageClair=""

adecrypter=MessageCrypte.upper()

for i in range(lg):
    if adecrypter[i]==' ':
        MessageClair+=' '
    else:
        asc=ord(adecrypter[i])-cle
        MessageClair+=chr(asc+26*((asc<65)-(asc>90)))

print (MessageClair.lower())
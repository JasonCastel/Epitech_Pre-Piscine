Messageacrypter=input("Saisissez un mot à chiffrer: ")
cle=int(input("Choisissez la clé caesar: "))

acrypter=Messageacrypter.upper()
lg=len(acrypter)
MessageCrypte=""

for i in range(lg):
    if acrypter[i]==' ':
        MessageCrypte+=' '
    else:
        asc=ord(acrypter[i])+cle
        MessageCrypte+=chr(asc+26*((asc<65)-(asc>90)))

print (MessageCrypte.lower())
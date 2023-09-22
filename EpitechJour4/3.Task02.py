Messageacrypter=input()
cle=input()

acrypter=Messageacrypter.upper()
cle2=cle.upper()
lg=len(acrypter)
MessageCrypte=""

for i in range(lg):
    if acrypter[i]==' ':
        MessageCrypte+=' '
    else:
        asc=ord(acrypter[i])+ord(cle2[i])
        MessageCrypte+=chr(asc+26*((asc<65)-(asc>90)))

print (MessageCrypte.lower())
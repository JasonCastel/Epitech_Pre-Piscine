user=int(input("Entrez un nombre: "))

if (user == 42) or (user<=21) or ((user % 2)==0) or ((user/2)<21) or (((user % 2) != 0) and user>45):
    print("OK")
else:
    print("You got wrong my poor friend!")



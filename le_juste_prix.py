from random import randint 
mystere=randint(1,1000)

for i in range(1,11):
    entree=int(input("Tente ta chance: \n"))
    vies=10-i
    if i != 10:
        if entree < mystere:
            print("C'est plus! Attention il te reste", vies,"vies")
        elif entree > mystere:
            print("C'est moins! Attention il te reste", vies, "vies")
        else:
            break

if entree != mystere:
    print("You loose")
else:
    print("You won!")
    
print("Le nombre mystere etait", mystere)

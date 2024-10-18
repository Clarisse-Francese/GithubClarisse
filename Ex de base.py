## Rappels de base
# Ex 1 : Écrire  un programme Python permettant de saisir deux nombres et d'afficher leur produit.  
x = int(input("Entrez le premier nombre : "))
y = int(input("Entrez le deuxième nombre : "))
print("Le produit de",x,"et",y,"est",x*y)

# Ex 2 : Écrire un un programme Python qui  permet d'afficher si un nombre  entier saisi au  clavier est pair ou impair. 
x = int(input("Entrez un nombre : "))
if x%2 == 0 :
   print(x,"est un nombre pair")
else : 
    print(x,"est un nombre impair")

# Ex 3 : Écrire un programme Python  qui permet d'afficher le plus grand de trois entiers saisis  au clavier.
a = int(input("Entrez un 1er nombre : "))
b = int(input("Entrez un 2eme nombre : "))
c = int(input("Entrez un 3eme nombre : "))
if a > b and a > c : 
    print(a,'est le plus grand nombre parmi',a,b,'et',c)
elif b > a and b > c : 
    print (b,'est le plus grand nombre parmi',a,b,'et',c)
else : 
    print (c,'est le plus grand nombre parmi',a,b,'et',c)

# Ex 4 : Une boutique propose à ses clients, une réduction de 15% pour les montants d’achat supérieurs à 200 euros. Écrire un programme Python permettant de saisir le prix total HT et de calculer le  montant TTC en prenant en compte la réduction et la TVA=20%.
m =  float(input("Saisir le montant total HT : "))
mttc = m*1.2
if mttc > 200 :
    mttc = mttc*0.85
print ("Le montant TTC est de",mttc,"euros")

## Boucle while
# Ex 5 : Écrire un programme Python qui permet  d'afficher  le message "Bonsoir" 5 fois. Utilisant la boucle while.
i = 0
while i <= 4 :
    print("Bonsoir")
    i += 1

# Ex 6 : Écrire un programme Python permettant de  calculer la somme   S=1+2+3+...+ N,  où N saisi par l’utilisateur.  Utilisant la  boucle while.
N = int(input("Entrez un entier : "))
i = 1
S = 0
while i <= N : 
    S += i
    i += 1
print ("La somme de 1 jusqu'à",N, "vaut",S)

# Ex 7 : Écrire un programme Python qui permet d'inverser les chiffres d'un entier N saisi par l'utilisateur.   par exemple  N=35672  le résultat affiché doit être 27653 
N = str(input("Entrez un entier : "))
M = ""
i = len(N)-1
while i >=0 :
    M += N[i]
    i -= 1
print(M)

## Boucle for
# Ex 8 : Écrire un programme Python qui permet de  calculer  la somme  S=1+2+3+...+ 10. Utilisant la boucle for.
s = 0
for k in range (11) :
    s += k
print("La somme vaut",s)

# Ex 9 : Écrire un programme Python, entrez deux nombres de l'utilisateur et trouvez le plus grand diviseur commun en utilisant la boucle for.
N = int(input("Entrez un 1er entier : "))
M = int(input("Entrez un 2eme entier : "))
PGCD = 1
for k in range(1,min(M,N)+1) :
    if M%k == 0 and N%k == 0 :
        PGCD = k
print("Le plus grand diviseur commun entre",M,"et",N,"est",PGCD)

# Tableaux
# Ex 10 : Écrire un programme Python pour déclarer et initialiser un tableau, puis saisir ses éléments à partir de l'utilisateur et afficher le tableau.
import numpy as np 
N = int(input("Entrez le nombre d'élément du tableau : "))
T = [0]*N
for i in range (N):
    A = int(input("Entrez l'élement {0}: ".format(i+1)))
    T[i] = A
print(T)

# Ex 11 : Écrire un programme Python pour déclarer un tableau, puis saisir ses éléments à partir de l'utilisateur et rechercher l'élément le plus grand et le deuxième dans ce tableau.
import numpy as np 
N = int(input("Entrez le nombre d'élément du tableau : "))
T = [0]*N
for i in range (N):
    A = int(input("Entrez l'élement {0}: ".format(i+1)))
    T[i] = A
max1 = max2 = min(T)
for i in range (N) : 
    if T[i] > max1 :
        max1 = T[i]
for i in range (N) :
    if T[i] > max2 and T[i] < max1 :
        max2 = T[i]
print("Le plus grand élément est :",max1,"et le deuxième plus grand est",max2)

# Ex 12

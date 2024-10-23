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
print("Le plus grand élément est ",max1,"et le deuxième plus grand est",max2)

# Ex 12 : Un gardien de phare va aux toilettes cinq fois par jour. Or les WC sont au rez-de-chaussée… Écrire une procédure (donc sans return) hauteurParcourue qui reçoit deux paramètres, le nombre de marches du phare et la hauteur de chaque marche (en cm), et qui affiche : Pour x marches de y cm, il parcourt z.zz m par semaine.

n = int(input("Combien il y a-t-il de marches ? "))
h = int(input("Quelle est la hauteur de chaque marche en cm ? "))

def hauteurParcourue(n,h) :
    print("Pour",n,"marches de",h,"cm, il parcourt", (n*h*2*5*7)/100,"m dans la semaine")

hauteurParcourue(n,h)

# Ex 13 : Dans la série "Kaamelott" d'Alexandre Astier, le "cul de chouette" est le jeu favori du tavernier et du chevalier Karadoc. Le but présumé de ce jeu est de jeter des dés en tentant d'atteindre un certain total par jet. Le but de cet exercice est d'écrire une fonction qui, pour une valeur donnée, renvoie toutes les solutions de 3 dés (dés classiques allant de 1 à 6) pouvant donner cette valeur. Attention, les solutions doivent être uniques. Si la solution (1, 2, 3) convient pour la valeur 6 alors la solution (2, 3, 1) ne peut plus convenir (les dés sont interchangeables). Aide: renvoyer plusieurs valeurs consiste à créer un tableau et à le remplir durant la recherche puis au final retourner le tableau.

def cul_de_chouette (valeur) :
    res = list()
    for i in range (1,7):
        for j in range (i,7):
            for k in range (j,7):
                if k+i+j == valeur :
                    res.append((i,j,k))
                    
    return res

n = int(input("Quelle est la valeur à atteindre ? "))
print("Les combinaisons de dés possibles pour faire", n,"sont",cul_de_chouette(7))
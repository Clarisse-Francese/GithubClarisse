ctrl + / # pour mettre en commentaire
Shift + Enter en sélectionnant du code # run que le code sélectionné

m = 1 # affectation
p = 1
y = "Bonjour"
A = 'abra'  et B= 'cad'  A+B+A = 'abracadabra'

nombre = int(4.6) # transforme en entier : 4
float(-6) # transofme en réel : -6,0
str(nombre) # transforme en caractère : '4'
abs(-7) # donne la valeur absolue : 7

+, -, *, ** (puissance), e-5, pow(x,y) #x à la puissance y
7//2 # division euclidienne (quotient) : 3 (car 7 = 3x2+1)
7%2 # reste ou modulo (utile pour paire ou impaire) : 1
from math import * 
pi, e, sqrt, exp, log, log10, factorial, sin, cos ...

==   !=  <  >  <=   >=
not  and   or  #renvoient des Boléens Truc  False
b in L # cherche l'élement b dans L, renvoie un boléen False ou True

\n # retour à la ligne

n = int(input("Entrez un nombre "))
# si plusieurs nombre à rentrer, boucle for :
for i in range (N):
    A = int(input("Entrez l'élement {0}: ".format(i+1)))
    formule avec A

print("Le nombre n vaut",n)

if :    elif :     else :     #bien respecter l'indentation

for k in range (m,n) : # k prend successivement les valeurs entières de m à n-1 
for k in range(m) : # k va de 0 à m-1   
for k in range (m,n,p) : # k va de m à n-1 avec un pas de p
for k in [1,2,3,4] : # k prend chaque valeur de la liste
    
c = 0
for lettre in "mot" : 
    c += 1

d = 0
while d < 9 :
    d += 2

L = [] # définition d'une liste vide
L = [a,b,c,d] # définition de la liste A
len(L) # renvoie 4
L[0] # renvoie a
L[0,2] # renvoie [a,b] car renvoie L du a-ième élement au (b-1)ième élément
L[1:] # va jusqu'à la fin 
L[:3] # à partir du début
L[:-1] # L privé de son dernier élement
L.append(3) # ajoute 3 à la fin de la liste
L.insert(2,3) # ajoute 3  à l'indice 2
L.pop(2) # retourne l'élément d'indice 2 et le retire de L
L.index(A) # retourne l'indice de l'élément A dans L
L.count(A) # compte le nombre d'occurence de A dans L
L.sort() # trie la liste L
L.reverse() #inverser l'ordre des élements de L

def NomFonction(argument1,argument2):
    """Documentation sur ce que fait la fonction, entrées, sorties"""
    return("Fonction exécutée")

import random
random.random() # renvoie un réel entre 0 et 1
random.randint(a,b) # renvoie un entier entre [a,b]
random.uniform(a, b) # renvoie un nombre flottant aléatoire entre a et b
random.choice(seq) # sélectionne un élément aléatoire d'une séquence (liste, chaîne, etc.)
random.shuffle(seq) # mélange les éléments d'une liste sur place

pip install numpy # à taper dans le terminal avant car numpy n'est pas une bibliothèque de base de Python
import numpy as np 
A = np.array([[1,2,3],[4,5,6]])
T = [0]*4 # [0,0,0,0]
np.zeros((2,3)) # crée un tableau rempli de 0
np.ones((4,5)) # crée un tableau rempli de 1
np.arange(3,6) # crée le tableau [3,4,5,6]
np.linspace(0,1,0.2) # [0,0.2,0.4,0.6,0.8,1] tableau et subdivision
np.reshape() # redimensionne un tableau
np.mean() # calcule la moyenne d'un tableau.
np.sum() # somme les éléments du tableau.
np.dot() # produit scalaire entre deux tableaux
nouveau tableau = np.append(tableau,4) # ajoute l'élement 4 à tableau dans un nouveau tableau
A.ndim # renvoie nombre de dimension d'un tableau. Ici 2
A.shape # renvoie les dimensions du tableau A.shape[0] : nombre ligne et A.shape [1] : nombre colonne. Ici (2,3)

# Rq syntaxe : A.methode équivalent à np.methode(A)

# Pour appeler une fonction, la marquer dans le code, pas dans le terminal
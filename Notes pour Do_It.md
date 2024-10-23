# Horodatage

Jeudi 17/10
30 min : création de mon espace Github sur Visual studio code (avec l'aide de ChatGPT)
1h : relecture de ma fiche informatique de prépa, rédaction de Rappels Python
1h30 : ex 1 à 9 réalisés

Vendredi 18/10
1h30 : importation bibliothèques numpy et random, ex 10 et 11

Mercredi 23/10
1h : ex 12 et 13
1h - ex inventé et résolu avec l'aide de ChatGPT
début 16h20 : rédaction

## Sites

[Lien 1](https://www.coodemaroc.com/2021/09/python.html) : premier site utilisé  
[Lien 2](https://python.developpez.com/exercices/)

## 
Demandes envers ChatGPT

créé moi un dictionnaire sur python avec 2 valeurs :
- Prénoms triés par odre alphabétique : 
Mathis, Mbaye, Baptiste, Clarisse, Damien, Emma, Valentin, Sophia, Charles, Matthieu, Jeanne, Juliette, Kévin, Alix, Lola, Manuela, Loïck, Esther, Inès, Isée, Thomas, Guillaume, Titouan, Sofiane, Victor
- Couleur : 
aléatoirement attribué entre "bleu", "vert" et "saumon"

promo = {'Alix': 'saumon', 'Baptiste': 'vert', 'Charles': 'saumon', 'Clarisse': 'bleu', 'Damien': 'vert', 'Emma': 'bleu', 'Esther': 'vert', 'Guillaume': 'bleu', 'Inès': 'vert', 'Isée': 'bleu', 'Jeanne': 'saumon', 'Juliette': 'vert', 'Kévin': 'bleu', 'Lola': 'vert', 'Loïck': 'saumon', 'Manuela': 'saumon', 'Mathis': 'saumon', 'Matthieu': 'bleu', 'Mbaye': 'saumon', 'Sofiane': 'saumon', 'Sophia': 'bleu', 'Thomas': 'saumon', 'Titouan': 'bleu', 'Valentin': 'vert', 'Victor': 'vert'}

J'ai alors modifié le tableau pour mettre des couleurs plus cohérente avec les élèves : 

promo = {'Alix': 'bleu', 'Baptiste': 'saumon', 'Charles': 'saumon', 'Clarisse': 'saumon', 'Damien': 'saumon', 'Emma': 'vert', 'Esther': 'bleu', 'Guillaume': 'bleu', 'Inès': 'saumon', 'Isée': 'saumon', 'Jeanne': 'saumon', 'Juliette': 'bleu', 'Kévin': 'vert', 'Lola': 'bleu', 'Loïck': 'vert', 'Manuela': 'vert', 'Mathis': 'vert', 'Matthieu': 'saumon', 'Mbaye': 'bleu', 'Sofiane': 'vert', 'Sophia': 'bleu', 'Thomas': 'vert', 'Titouan': 'bleu', 'Valentin': 'vert', 'Victor': 'saumon'}

Je veux une fonction qui prenne en entrée la promo et qui retourne en sortie 3 listes contenant chacun 8 élèves. Chaque liste doit être le mieux répartie possible entre les couleurs. Ainsi les profils bleu, saumon et vert sont équitablement répartis entre les 3 listes.

Est-ce que tu peux préciser entre parenthèse à coté de chaque prénom d'élève sa couleur associée
Est ce que à la fin tu peux ajouter un récap du nombre d'élève de chaque couleur dans chacun des groupes
Peux tu afficher le récapitulatif à la fin après la composition des groupes et supprimer les ' dans l'affichage des listes des groupes
Idem je veux que tu supprimes les ' dans l'affichage du récap des couleurs à la fin
Puis j'ai modifié manuellement quelques paramètres d'affichage comme mettre uniquement (b) au lieu de (bleu)

Voilà ce que la fonction renvoie :
Groupe 1: Guillaume (b), Emma (v), Victor (s), Titouan (b), Valentin (v), Matthieu (s), Mbaye (b), Kévin (v), Inès (s)
Groupe 2: Alix (b), Loïck (v), Damien (s), Juliette (b), Thomas (v), Isée (s), Lola (b), Manuela (v), Baptiste (s)
Groupe 3: Sophia (b), Mathis (v), Jeanne (s), Esther (b), Sofiane (v), Charles (s), Clarisse (s)

Récapitulatif des couleurs :
Groupe 1: bleu: 3 - vert: 3 - saumon: 3
Groupe 2: bleu: 3 - vert: 3 - saumon: 3
Groupe 3: bleu: 2 - vert: 2 - saumon: 3
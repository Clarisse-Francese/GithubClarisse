# Ex 14 : exo inventé par moi même, je veux créer un programme qui permettent de générer automatiquement 3 groupes de 8 élèves en Do_It qui sont équitablement répartis en profil de vert, bleu et saumon.

import random

def repartir_groupes(promo):
    bleu = [prenom for prenom, couleur in promo.items() if couleur == 'bleu']
    vert = [prenom for prenom, couleur in promo.items() if couleur == 'vert']
    saumon = [prenom for prenom, couleur in promo.items() if couleur == 'saumon']
    
    random.shuffle(bleu)
    random.shuffle(vert)
    random.shuffle(saumon)

    groupes = [[] for _ in range(3)]  # 3 groupes
    couleur_counts = [{ 'bleu': 0, 'vert': 0, 'saumon': 0 } for _ in range(3)]  # Compteur pour chaque groupe

    for i in range(8):  # 8 élèves par groupe
        for j in range(3):  # Répartir entre les 3 couleurs
            if len(bleu) > 0:
                groupes[j].append(f"{bleu.pop()} (b)")
                couleur_counts[j]['bleu'] += 1
            if len(vert) > 0:
                groupes[j].append(f"{vert.pop()} (v)")
                couleur_counts[j]['vert'] += 1
            if len(saumon) > 0:
                groupes[j].append(f"{saumon.pop()} (s)")
                couleur_counts[j]['saumon'] += 1

    return groupes, couleur_counts

# Exemple d'utilisation
promo = {'Alix': 'saumon', 'Baptiste': 'vert', 'Charles': 'saumon', 'Clarisse': 'bleu', 'Damien': 'vert', 'Emma': 'bleu', 'Esther': 'vert', 'Guillaume': 'bleu', 'Inès': 'vert', 'Isée': 'bleu', 'Jeanne': 'saumon', 'Juliette': 'vert', 'Kévin': 'bleu', 'Lola': 'vert', 'Loïck': 'saumon', 'Manuela': 'saumon', 'Mathis': 'saumon', 'Matthieu': 'bleu', 'Mbaye': 'saumon', 'Sofiane': 'saumon', 'Sophia': 'bleu', 'Thomas': 'saumon', 'Titouan': 'bleu', 'Valentin': 'vert', 'Victor': 'vert'}

groupes, couleur_counts = repartir_groupes(promo)
for i, groupe in enumerate(groupes):
    print(f"Groupe {i + 1}: {', '.join(groupe)}")

# Affichage du récapitulatif des couleurs sans apostrophes
print("\nRécapitulatif des couleurs :")
for i in range(3):
    print(f"Groupe {i + 1}: bleu: {couleur_counts[i]['bleu']} - vert: {couleur_counts[i]['vert']} - saumon: {couleur_counts[i]['saumon']}")

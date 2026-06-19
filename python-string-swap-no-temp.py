#Écrire un programme Python qui permet de saisir deux chaînes de caractères puis de 
#permuter leurs contenus sans utiliser une variable auxiliaire.

def long(chaine):
    compteur = 0
    for caractere in chaine:
        compteur += 1
    return compteur

# Saisie des deux chaînes de caractères
CH1 = input("Donner la première chaîne (CH1) : ")
CH2 = input("Donner la deuxième chaîne (CH2) : ")

# Affichage avant permutation
print(f'Avant permutation : CH1 = "{CH1}" et CH2 = "{CH2}"')

# Garder les longueurs initiales en utilisant la fonction long
longueur_ch1_initiale = long(CH1)
longueur_ch2_initiale = long(CH2)

# Étape 1: Concaténer CH1 et CH2 dans CH1
# Si CH1="Ali" et CH2="Sami", CH1 devient "AliSami"
CH1 = CH1 + CH2

# Étape 2: Extraire l'ancienne valeur de CH1 de la nouvelle CH1 pour la mettre dans CH2
# CH2 = "AliSami"[:(longueur_ch1_initiale + longueur_ch2_initiale) - longueur_ch2_initiale] -> "AliSami"[:longueur_ch1_initiale] -> "Ali"
CH2 = CH1[:longueur_ch1_initiale]

# Étape 3: Extraire l'ancienne valeur de CH2 de la nouvelle CH1 pour la mettre dans CH1
# CH1 = "AliSami"[longueur_ch1_initiale:] -> "Sami"
CH1 = CH1[longueur_ch1_initiale:]

# Affichage après permutation
print(f'Après permutation : CH1 = "{CH1}" et CH2 = "{CH2}"')
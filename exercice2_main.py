# L'énoncé de l'exercice
'''
Dans cet exercice, vous allez créer un programme qui calcule les frais d'un voyage. Le
programme contient deux fichiers:
1 - Un module (voyage) contenant la définition des fonctions qui calculent les différents
frais.
2 - Un fichier principal (main) qui demande à l'utilisateur de saisir les données du voyage
et calcule le total des frais.
'''
# la solution corrigée de l'exercice
from exercice2_voyage import *
nombre_nuits = int(input('Veuillez entrer le nombre de nuits : '))
nombre_jours = int(input('Veuillez entrer le nombre de jours : '))
nom_ville = input('Veuillez entrer le nom de la ville (Marrakech, Paris, Oran, Carthage, Dakar) : ')
autres_frais = float(input("Veuillez entrer d'autres frais du voyage : "))
# Affichage
print(f"Le coût total du voyage est : {voyage_frais(nombre_nuits, nombre_jours, nom_ville, autres_frais)} Euro.")
# L'énoncé de l'exercice
'''
Dans cet exercice, vous allez créer un programme qui vous permet d'effectuer des calculs
statistiques sur les notes de 5 étudiants (sans utiliser le module standard statistics). Le
programme doit contenir deux fichiers:
1 - Un module (stats) contenant la définition des fonctions statistiques suivantes: somme,
moyenne, variance, écart-type et coefficient de variation.
2 - Un fichier principal (main) qui demande à l'utilisateur de saisir les 5 notes, appelle les
fonctions et affiche les résultats statistiques.
'''
# la solution corrigée de l'exercice
from exercice1_stats import *
#Lire les valeurs
note1 = float(input('Veuillez entrer la note 1 : '))
note2 = float(input('Veuillez entrer la note 2 : '))
note3 = float(input('Veuillez entrer la note 3 : '))
note4 = float(input('Veuillez entrer la note 4 : '))
note5 = float(input('Veuillez entrer la note 5 : '))
# Affichage
print(f"La somme des 5 notes est : {somme(note1, note2, note3, note4, note5)}")
print(f"La moyenne des 5 notes est : {moyenne(note1, note2, note3, note4, note5)}")
print(f"La variance des 5 notes est : {variance(note1, note2, note3, note4, note5)}")
print(f"L'écart-type  des 5 notes est : {ecart_type(note1, note2, note3, note4, note5)}")
print(f"Le coefficient de variation des 5 notes est : {coefficient_variation(note1, note2, note3, note4, note5)} %")
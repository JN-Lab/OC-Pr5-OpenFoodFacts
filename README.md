# OC-Pr5-OpenFoodFacts
Il s'agit du Repository pour le projet 5 du parcours Développeur d'Application Python (Openclassrooms)

## Présentation
Il s'agit d'un programme permettant à un internaute de fournir un aliment de substitution plus sain que celui sélectionné.
Pour cela, le programme s'appuie sur les données de la base OpenFoodFacts.

## Description du parcours utilisateur
L'utilisateur ouvre le programme, ce dernier lui affiche les choix suivantes:
1. Quel aliment souhaitez-vous remplacer?
1. Retrouver mes aliments substitués.

L'utilisateur sélectionne 1. Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses :
* Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
* Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]
* Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.
* L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.

## Fonctionnalité
* Recherche d'aliments dans la base Open Food Facts.
* L'utilisateur interagit avec le programme dans le terminal ou via une interface graphique.
* Si l'utilisateur entre un caractère qui n'est pas un chiffre, le programme doit lui répéter la question.
* La recherche doit s'effectuer sur une base MySql.

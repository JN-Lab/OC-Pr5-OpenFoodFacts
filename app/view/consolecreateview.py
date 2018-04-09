#! /usr/bin/env python3
# coding: utf-8

class ConsoleCreateView:
    """ This class groups all the console's messages linked to database creation """

    def start_db_creation(self):
        print("Création des bases de données")

    def start_get_categories(self):
        print("Récupération des catégories pertinentes. Veuillez patienter s'il vous plait")

    def end_creation(self):
        print("Création de la base de données terminées.")

#! /usr/bin/env python3
# coding: utf-8

class ConsoleCreateView:

    def __init__(self):
        pass

    def start_db_creation(self):
        print("Création des bases de données")

    def start_get_categories(self):
        print("Récupération des catégories pertinentes. Veuillez patienter s'il vous plait")

    def start_feed_product(self):
        print("Récupération des produits par catégories. Cela peut prendre quelques minutes")

    def end_creation(self):
        print("Création de la base de données terminées.")

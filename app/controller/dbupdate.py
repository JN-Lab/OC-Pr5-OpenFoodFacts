#! /usr/bin/env python3
# coding: utf-8
import datetime
from model.update_db import LogDatabase
from model.product import ProductDatabase
from model.registered_product import RegisteredProductDatabase
from model.category import CategoryDatabase

class UpdateDatabase:

    def __init__(self):
        self.daily_date = datetime.date.today()
        self.db_registered_product = RegisteredProductDatabase()
        self.db_update = LogDatabase()
        self.db_category = CategoryDatabase()
        self.db_product = ProductDatabase()
        self.update = self.__update_decision()

    def update_database(self):
        """This method updates the database with modification identified in API response """
        if self.update:
            saved_products_ref_tuple = self.db_registered_product.get_product_ref()
            print(saved_products_ref_tuple)
            print(type(saved_products_ref_tuple))

            #We delete registered_product and product tables and recreate them empty
            self.db_registered_product.create_db()
            self.db_product.create_db()
            self.db_registered_product.create_keys()

            #We get the categories from the database
            categories_tuple = self.db_category.get_categories()
            for category in categories_tuple:
                pass


        # Si update_decision is True
        # Je récupère les ref des produits enregistrés dans un tableau
        # Je supprime la base produit et produits enregistrés
        # Je les recrées
        # Pour chaque catégorie dans la db:
            #je relance la procédure d'injection produit présent dans db creation sa race (a initier dans __init__)
        # Pour chaque produits enregistrés dans la liste:
            #s'il est présent dans la table produit:
                #je le réinjecte avec le statut Disponible
            #sinon, je le réinjecte avec le statut plus disponible

    def __update_decision(self):
        """ This method decides if an update of the database has to be done """
        last_update_date = self.db_update.get_last_update_date() #type: datetime.date
        duration = self.daily_date - last_update_date #type: datetime.timedelta

        if duration.days >= 0:
            return True

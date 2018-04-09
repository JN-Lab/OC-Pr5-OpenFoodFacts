#! /usr/bin/env python3
# coding: utf-8
import datetime
from model.update_db import LogDatabase
from model.product import ProductDatabase
from model.registered_product import RegisteredProductDatabase
from model.category import CategoryDatabase
from view.consoleupdateview import ConsoleUpdateView
from .dbinjection import InjectData

class UpdateDatabase:
    """ This class manages all the actions linked to the update of the database """

    def __init__(self):
        self.daily_date = datetime.date.today()
        self.db_registered_product = RegisteredProductDatabase()
        self.db_update = LogDatabase()
        self.db_category = CategoryDatabase()
        self.db_product = ProductDatabase()
        self.db_injection = InjectData()
        self.interface = ConsoleUpdateView()

        self.update = self.__update_decision()

    def update_database(self, force=False):
        """ This method updates the database with modification identified in API response """
        if self.update or force:
            self.interface.start_update()
            saved_products_ref_list = self.db_registered_product.get_products_ref()

            #We delete registered_product and product tables and recreate them empty
            self.db_registered_product.create_db()
            self.db_product.create_db()
            self.db_product.create_keys()
            self.db_registered_product.create_keys()

            #We feed the products for each get_categories
            self.interface.start_feed_product()
            self.db_injection.feed_products()

            #for each ref from saved_products_ref_tuple:
            for product_ref in saved_products_ref_list:
                product_id = self.db_product.select_product_from_ref(product_ref)
                print(product_ref)
                if product_id:
                    print('injection produit disponible')
                    self.db_registered_product.inject_product(product_ref, 'disponible')
                else:
                    print('injection produit indisponible')
                    self.db_registered_product.inject_product(product_ref, 'indisponible')

            #Don't forget to update the update date
            self.db_update.inject_update_date()
            self.interface.end_update()

    def __update_decision(self):
        """ This method decides if an update of the database has to be done """
        last_update_date = self.db_update.get_last_update_date() #type: datetime.date
        duration = self.daily_date - last_update_date #type: datetime.timedelta

        if duration.days >= 7:
            return True

#! /usr/bin/env python3
# coding: utf-8

from model.product import ProductDatabase
from model.category import CategoryDatabase
from model.registered_product import RegisteredProductDatabase
from model.update_db import UpdateDatabase

class CreateDatabase:

    def __init__(self):
        self.db_registered_product = RegisteredProductDatabase()
        self.db_product = ProductDatabase()
        self.db_category = CategoryDatabase()
        self.db_update = UpdateDatabase()


    def prepare(self):
        """ This method creates all the necessary databases for the application """

        # Databases are created
        self.db_registered_product.create_db()
        self.db_product.create_db()
        self.db_category.create_db()
        self.db_update.create_db()

        # Foreign keys are Created
        self.db_registered_product.create_keys()

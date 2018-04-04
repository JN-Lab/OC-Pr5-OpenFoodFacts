#! /usr/bin/env python3
# coding: utf-8

from model.product import ProductDatabase
from model.category import CategoryDatabase
from model.registered_product import RegisteredProductDatabase
from model.update_db import LogDatabase
from view.consolecreateview import ConsoleCreateView
from .dbinjection import InjectData

class CreateDatabase:

    def __init__(self):
        self.db_registered_product = RegisteredProductDatabase()
        self.db_product = ProductDatabase()
        self.db_category = CategoryDatabase()
        self.db_update = LogDatabase()
        self.db_injection = InjectData()
        self.interface = ConsoleCreateView()

    def prepare(self):
        """ This method creates all the necessary databases for the application """

        # Databases are created
        self.interface.start_db_creation()
        self.db_registered_product.create_db()
        self.db_product.create_db()
        self.db_category.create_db()
        self.db_update.create_db()

        # Foreign keys are created
        self.db_registered_product.create_keys()

        # Databases are feed
        self.interface.start_get_categories()
        self.db_injection.feed_categories()
        self.db_injection.feed_products()

        # Update date is registered
        self.db_update.inject_update_date()
        self.interface.end_creation()

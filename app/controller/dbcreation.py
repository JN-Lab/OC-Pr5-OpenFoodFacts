#! /usr/bin/env python3
# coding: utf-8

from model.product import ProductDatabase
from model.category import CategoryDatabase

class CreateDatabase:

    def __init__(self):
        self.db_product = ProductDatabase()
        self.db_category = CategoryDatabase()

    def prepare(self):
        self.db_product.create_db()
        self.db_category.create_db()

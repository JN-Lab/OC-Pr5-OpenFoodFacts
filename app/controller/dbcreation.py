#! /usr/bin/env python3
# coding: utf-8

from model.product import ProductDatabase
from model.category import CategoryDatabase
from model.registered_product import RegisteredProductDatabase
from model.update_db import UpdateDatabase
from .api_interaction import OpenFoodFactsInteractions

class CreateDatabase:

    def __init__(self):
        self.db_registered_product = RegisteredProductDatabase()
        self.db_product = ProductDatabase()
        self.db_category = CategoryDatabase()
        self.db_update = UpdateDatabase()
        self.api = OpenFoodFactsInteractions()


    def prepare(self):
        """ This method creates all the necessary databases for the application """

        # Databases are created
        self.db_registered_product.create_db()
        self.db_product.create_db()
        self.db_category.create_db()
        self.db_update.create_db()

        # Foreign keys are created
        self.db_registered_product.create_keys()

    def feed_categories(self):
        """ This method injects the categories from OpenFoodFacts into the database """

        self.api.get_categories()
        self.db_category.inject_categories(self.api.category_list)

    def feed_products(self):
        """ This method injects the products linked to the categories selected
        into the database """

        page_size = 1000
        for category in self.api.category_list:
            page_number = self.api.get_product_pages_number(category, str(page_size)) # A créer
            for page in range(1, page_number + 1, 1):
                data = self.api.get_product_page(category, str(page_size), str(page)) # A créer
                self.__manage_products_injection(data['products'], category) # A créer

    def __manage_products_injection(self, data, category):
        print("Injection des produits de la catégorie {}".format(category))
        for product in data:
            product_info = self.__get_product_information(product)
            if product_info['injection']:
                self.db_product.inject_product(product_info, category)

    def __get_product_information(self,product):
        """ This method cleans and get the needed product informations """

        product_info = {
            'injection' : True,
            'url' : '',
            'score' : '',
            'name' :'',
            'ref' : '',
            'store' : '',
            'description' : ''
        }

        try:
            product_info['url'] = product['url']
        except KeyError:
            product_info['url'] = 'NULL'

        try:
            product_info['score'] = product['nutrition_grade_fr']
        except KeyError:
            product_info['score'] = 'NULL'
            product_info['injection'] = False

        try:
            product_info['name'] = product['product_name_fr']
        except KeyError:
            product_info['name'] = 'NULL'
            product_info['injection'] = False

        try:
            product_info['ref'] = product['code']
        except KeyError:
            product_info['ref'] = 'NULL'
            product_info['injection'] = False

        try:
            product_info['store'] = product['stores']
        except KeyError:
            product_info['store'] = 'NULL'

        try:
            product_info['description'] = product['generic_name_fr']
        except KeyError:
            product_info['description'] = 'NULL'

        return product_info

#! /usr/bin/env python3
# coding: utf-8

from model.category import CategoryDatabase
from model.product import ProductDatabase
from view.consoleapplicationview import ConsoleApplicationView

class Application:

    def __init__(self):
        self.interface = ConsoleApplicationView()
        self.db_category = CategoryDatabase()
        self.db_product = ProductDatabase()

        self.cat_information = ()
        self.cat_id_selected = 0

        self.prd_tuple = ()
        self.prd_id_selected = 0

    def category_selection(self):
        """ This method manages the category selection """

        self.cat_information = self.db_category.get_categories_with_id()
        self.interface.category_selection(self.cat_information)
        while self.cat_id_selected < 1 or self.cat_id_selected > len(self.cat_information):
            try:
                self.cat_id_selected = int(input("numéro de la catégorie: "))
            except:
                self.interface.error_input_not_int()
        self.interface.category_selected(self.cat_information, self.cat_id_selected)

    def product_selection(self):
        """ This method manages the product selection """

        self.prd_tuple = self.db_product.get_dirty_product_from_category(self.cat_id_selected)
        self.interface.product_selection(self.prd_tuple)
        prd_number = 0
        while prd_number < 1 or prd_number > len(self.prd_tuple):
            try:
                prd_number = int(input("numéro de produit: "))
            except:
                self.interface.error_input_not_int()

        #prd_number - 1 because index starts from zero
        self.prd_id_selected = self.prd_tuple[prd_number - 1][0]
        self.interface.product_selected(self.prd_tuple, prd_number - 1)

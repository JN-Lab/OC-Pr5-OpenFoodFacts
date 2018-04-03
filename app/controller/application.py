#! /usr/bin/env python3
# coding: utf-8

from model.category import CategoryDatabase
from view.consoleapplicationview import ConsoleApplicationView

class Application:

    def __init__(self):
        self.interface = ConsoleApplicationView()
        self.db_category = CategoryDatabase()
        self.cat_information = ()
        self.cat_id_selected = 0

    def category_selection(self):
        self.cat_information = self.db_category.get_categories_with_id()
        self.interface.category_selection(self.cat_information)
        while self.cat_id_selected < 1 or self.cat_id_selected > len(self.cat_information):
            try:
                self.cat_id_selected = int(input("numéro de la catégorie: "))
            except:
                self.interface.error_input_not_int()

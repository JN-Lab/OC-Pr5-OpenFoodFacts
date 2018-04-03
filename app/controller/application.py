#! /usr/bin/env python3
# coding: utf-8

from model.category import CategoryDatabase
from view.consoleapplicationview import ConsoleApplicationView

class Application:

    def __init__(self):
        self.interface = ConsoleApplicationView()
        self.db_category = CategoryDatabase()
        self.categories_information = ()

    def category_selection(self):
        self.categories_information = self.db_category.get_categories_with_id()
        self.interface.category_selection(self.categories_information)

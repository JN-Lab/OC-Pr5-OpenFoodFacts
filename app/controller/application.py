#! /usr/bin/env python3
# coding: utf-8

from model.category import CategoryDatabase
from model.product import ProductDatabase
from model.registered_product import RegisteredProductDatabase
from view.consoleapplicationview import ConsoleApplicationView
from .dbupdate import UpdateDatabase

class Application:

    def __init__(self):
        self.interface = ConsoleApplicationView()
        self.db_category = CategoryDatabase()
        self.db_product = ProductDatabase()
        self.db_registered_product = RegisteredProductDatabase()
        self.update = UpdateDatabase()

        self.cat_information = ()
        self.cat_id_selected = 0
        self.prd_tuple = ()
        self.subst_prd_tuple = ()

        self.play = True

    def start(self):
        """ This method manages the different steps of the application"""
        while self.play:
            self.update.update_database()
            action = self.action_choice()
            if action == 'research':
                self.category_selection()
                self.product_selection()
                self.selected_substitute_products()
                self.save_substitute_product()
            else:
                self.consult_product_saved()
            #Quit or new action?
            self.new_action()

    def category_selection(self):
        """ This method manages the category selection """
        self.cat_id_selected = 0 #to be sure to ask category each time
        self.cat_information = self.db_category.get_categories_with_id()
        self.interface.print_category_selection(self.cat_information)
        while self.cat_id_selected < 1 or self.cat_id_selected > len(self.cat_information):
            try:
                self.cat_id_selected = int(input("numéro de la catégorie: "))
            except:
                self.interface.print_error_input_not_int()
        self.interface.print_category_selected(self.cat_information, self.cat_id_selected)

    def product_selection(self):
        """ This method manages the product selection """

        self.prd_tuple = self.db_product.get_dirty_product_from_category(self.cat_id_selected)
        print(self.prd_tuple)
        self.interface.print_product_selection(self.prd_tuple)
        prd_number = self.__prd_input(self.prd_tuple)
        #prd_number - 1 because index starts from zero
        self.interface.print_product_selected(self.prd_tuple, prd_number - 1)

    def selected_substitute_products(self):
        """ This method manages the selection of substitute products """

        self.subst_prd_tuple = self.db_product.get_subsitute_products(self.cat_id_selected)
        self.interface.print_subsitute_products(self.subst_prd_tuple)

    def save_substitute_product(self):
        """ This method manages the substitute product registered feature """

        save = True
        while save:
            self.interface.print_save_product_question()
            answer = 'W'
            while answer != 'Y' and answer != 'N':
                answer = input("Votre réponse: ").upper()

            if answer == 'Y':
                self.interface.print_product_to_save_question()
                prd_number = self.__prd_input(self.subst_prd_tuple)
                self.__product_save_process(self.subst_prd_tuple[prd_number - 1][5])
            else:
                save = False
                self.interface.print_end_save_process_message()

    def new_action(self):
        """ This method manages the process of reloading a research or stopping
        the application """
        self.interface.print_new_action()
        answer = 'W'
        while answer != 'Y' and answer != 'N':
            answer = input("Votre réponse: ").upper()

        if answer == 'Y':
            self.play = True
        else:
            self.play = False
            self.interface.print_good_bye_message()

    def action_choice(self):
        """This method manages the choice of the user between doing a research
        or seeing his saved products"""
        self.interface.print_action_choice()
        answer = 0
        while answer != 1 and answer != 2:
            try:
                answer = int(input("Votre choix:"))
            except:
                self.interface.print_error_input_not_int()

        if answer == 1:
            return 'research'

    def consult_product_saved(self):
        """ This method prints all the products saved by the user"""
        products = self.db_registered_product.get_all_products_saved()
        self.interface.print_products_saved(products)

    def __prd_input(self, product_tuple):
        """ This method manages the product selection """
        prd_number = 0
        while prd_number < 1 or prd_number > len(product_tuple):
            try:
                prd_number = int(input("numéro de produit: "))
            except:
                self.interface.print_error_input_not_int()

        return prd_number

    def __product_save_process(self, product_ref):
        """ This private method manages the process to save a product """
        product_to_save = self.db_registered_product.get_product_from_ref(product_ref)
        #Si le produit a déjà été enregistré
        if product_to_save:
            self.interface.print_product_already_saved()
        else:
            self.db_registered_product.inject_product(product_ref, 'disponible')
            self.interface.print_selected_product_to_save()

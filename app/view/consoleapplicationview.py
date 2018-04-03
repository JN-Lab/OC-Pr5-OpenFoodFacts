#! /usr/bin/env python3
# coding: utf-8

class ConsoleApplicationView:

    def __init__(self):
        pass

    def category_selection(self, category_tuple):
        """ This method prints in the terminal the product categories """

        print("\nVeuillez indiquer le chiffre associé à la catégories souhaitées:")
        for category in category_tuple:
            print("{} -> {}".format(category[0], category[1]))

    def category_selected(self, category_tuple, category_id):
        """ This method prints in the terminal the selected category """

        print("\nLa catégorie sélectionnée est {}".format(category_tuple[category_id - 1][1]))

    def product_selection(self, product_tuple):
        """ This method prints in the terminal the selected product from the
        selected category """

        print("\nVeuillez indiquer le chiffre associé au produit souhaité")
        for index, product in enumerate(product_tuple):
            #index + 1 because index starts from 0 and it is not very ergonomic
            print("{} -> {}".format(index + 1, product[1]))

    def product_selected(self, product_tuple, product_index):
        """ This method prints in the terminal the selected product """

        print("\nLe produit sélectionné est {}".format(product_tuple[product_index][1]))

    def error_input_not_int(self):
        """ This method prints an error message when the user indicates
        a string instead of a number """

        print("\nVeuillez indiquer le chiffre et non le nom de votre choix")

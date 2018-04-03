#! /usr/bin/env python3
# coding: utf-8

class ConsoleApplicationView:

    def __init__(self):
        pass

    def category_selection(self, category_tuple):
        print("Veuillez indiquer le chiffre associé à la catégories souhaitées:")
        for category in category_tuple:
            print("{} -> {}".format(category[0], category[1]))

    def error_input_not_int(self):
        print("Veuillez indiquer le chiffre et non le nom de la catégorie")

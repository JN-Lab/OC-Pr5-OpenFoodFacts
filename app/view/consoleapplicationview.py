#! /usr/bin/env python3
# coding: utf-8

class ConsoleApplicationView:

    def __init__(self):
        pass

    def category_selection(self, category_tuple):
        print("Veuillez indiquer le chiffres associés à la catégories souhaitées:")
        for category in category_tuple:
            print("{} -> {}".format(category[0], category[1]))

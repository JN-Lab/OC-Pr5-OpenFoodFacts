#! /usr/bin/env python3
# coding: utf-8

class ConsoleApiView:

    def __init__(self):
        pass

    def end_categories_selection(self, category_number, category_list):
        print("les {} catégories ont été sélectionnées".format(category_number))
        print("les catégories sélectionnées sont:")
        for category in category_list:
            print("-> {}".format(category))

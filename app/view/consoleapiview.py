#! /usr/bin/env python3
# coding: utf-8

class ConsoleApiView:
    """ This class manages the console's messages for the interactions with the API """

    def end_categories_selection(self, category_number, category_list):
        print("les {} catégories ont été sélectionnées".format(category_number))
        print("les catégories sélectionnées sont:")
        for category in category_list:
            print("-> {}".format(category))

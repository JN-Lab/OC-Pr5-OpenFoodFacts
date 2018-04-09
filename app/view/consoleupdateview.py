#! /usr/bin/env python3
# coding: utf-8

class ConsoleUpdateView:
    """ This class groups the console's messages linked to the database update """

    def start_update(self):
        """ This method indicates that the update starts """

        print("Début de la mise à jour des données")

    def start_feed_product(self):
        """ This method indicates that the products update starts """

        print("Mise à jour des produits. Veuillez patienter s'il vous plait.")

    def end_update(self):
        """ This method indicates the the update is over """

        print("Mise à jour des données terminées")

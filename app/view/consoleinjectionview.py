#! /usr/bin/env python3
# coding: utf-8

class ConsoleInjectionView:
    """ This class groups all the console's messages linked to database injections. """

    def product_injection_per_category(self, category):
        """ This method prints a message to indicate that the application
        injects the product of the X category """

        print("Injection des produits de la catégorie {}".format(category))
        print("Cela peut prendre un peu de temps. Veuillez patientez s'il vous plait.")

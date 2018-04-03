#! /usr/bin/env python3
# coding: utf-8

class ConsoleInjectionView:

    def __init__(self):
        pass

    def product_injection_per_category(self, category):
        print("Injection des produits de la catégorie {}".format(category))
        print("Cela peut prendre un peu de temps. Veuillez patientez s'il vous plait.")

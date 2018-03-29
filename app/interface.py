#! /usr/bin/env python3
# coding: utf-8

from dbconnexion import SQLconnexion

class Interface:

    def __init__(self):
        self.categories = self.__get_category_name()

    def __category_menu_console(self):
        print("\n ## BIENVENUE ## \n")
        print("Choisissez une catégorie d'aliments en indiquant le numéro correspondant:")
        for index, value in enumerate(self.categories):
            print('{}. {}'.format(index + 1, value))

    def __category_selection(self):
        choice = 0

        while choice < 1 or choice > len(self.categories):
            try :
                choice = int(input("Choix de la catégorie : "))
            except:
                print("Veuillez indiquer le numéro de la catégorie souhaitée")

        print("Vous avez choisi {}".format(self.categories[choice - 1]))

    def __get_category_name(self):
        categories = []

        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = 'SELECT category_name FROM Category'
                cursor.execute(sql)
                result = cursor.fetchall()
                for category in result:
                    categories.append(category[0])

        return categories

    def start(self):
        self.__category_menu_console()
        self.__category_selection()

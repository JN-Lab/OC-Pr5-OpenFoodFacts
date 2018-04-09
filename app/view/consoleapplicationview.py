#! /usr/bin/env python3
# coding: utf-8

class ConsoleApplicationView:
    """ This class manages the console's messages for the application features"""

    def print_category_selection(self, category_tuple):
        """ This method prints in the terminal the product categories """

        print("\nVeuillez indiquer le chiffre associé à la catégories souhaitées:")
        for category in category_tuple:
            print("{} -> {}".format(category[0], category[1]))

    def print_category_selected(self, category_tuple, category_id):
        """ This method prints in the terminal the selected category """

        print("\nLa catégorie sélectionnée est {}".format(category_tuple[category_id - 1][1]))

    def print_product_selection(self, product_tuple):
        """ This method prints in the terminal the selected product from the
        selected category """

        print("\nVeuillez indiquer le chiffre associé au produit souhaité")
        for index, product in enumerate(product_tuple):
            #index + 1 because index starts from 0 and it is not very ergonomic
            print("{} -> {}".format(index + 1, product[1]))

    def print_product_selected(self, product_tuple, product_index):
        """ This method prints in the terminal the selected product """

        print("\nLe produit sélectionné est {}".format(product_tuple[product_index][1]))

    def print_subsitute_products(self, substitute_product_tuple):
        """ This method prints in the terminale the selected substitute product """

        print("\nVoici les produits de subsitution que nous vous proposons:")
        for index, product in enumerate(substitute_product_tuple):
            print("{} -> Produit : {}".format(index + 1, product[0]))
            print("    - Description : {}".format(product[1]))
            print("    - Store : {}".format(product[2]))
            print("    - Url : {}".format(product[3]))
            print("    - Nutriscore : {}".format(product[4]))
            print("    - Code : {}".format(product[5]))
            print("\n")

    def print_save_product_question(self):
        """ This method prints prints a question for the user in order to know
        if he wants to save one product of substitution """

        print("""\nSouhaitez-vous enregitrer l'un des produits de substitution?
        (Y pour oui / N pour non)""")

    def print_product_to_save_question(self):
        """ This method asks to the user the number of the product to save """

        print("\n Veuillez indiquer le chiffre du produit à enregistrer")

    def print_selected_product_to_save(self):
        """ This method indicates to the user that the product had been saved """

        print("\n Le produit a été enregistré")

    def print_end_save_process_message(self):
        """ This method indicates to the user that the application goes back
        to the main menu """

        print("\n Retour au menu")

    def print_product_already_saved(self):
        """ This method indicates to the user that the product had already been
        saved """

        print("Le Produit a déjà été enregistré")

    def print_new_action(self):
        """ This method asks to the user if he wants to do another action """

        print("""\n Souhaitez-vous faire une nouvelle action?
        (Y pour oui / N pour non)""")

    def print_action_choice(self):
        """ This methods prints the different actions of the main menu"""

        print("\n Que souhaitez-vous faire?")
        print("   1 -> Chercher un produit de substitution")
        print("   2 -> Consulter vos produits enregistrés")
        print("""Veuillez indiquez le numéro correspondant à votre choix
         s'il vous plait""")

    def print_products_saved(self, product_tuple):
        """ This method prints all the saved products with their information """

        print("\nVoici les produits que vous avez enregistrés:")
        for index, product in enumerate(product_tuple):
            print("{} -> Produit : {}".format(index + 1, product[0]))
            print("    - Description : {}".format(product[1]))
            print("    - Store : {}".format(product[2]))
            print("    - Url : {}".format(product[3]))
            print("    - Nutriscore : {}".format(product[4]))
            print("    - Code : {}".format(product[5]))
            print("    - Etat : {}".format(product[6]))
            print("\n")

    def print_good_bye_message(self):
        """ This method prints a good-bye message """

        print("\n Merci d'avoir utilisé l'application. Au revoir")

    def print_error_input_not_int(self):
        """ This method prints an error message when the user indicates
        a string instead of a number """

        print("\n Veuillez indiquer le chiffre et non le nom de votre choix")

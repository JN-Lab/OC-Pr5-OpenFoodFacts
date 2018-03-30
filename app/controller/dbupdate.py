#! /usr/bin/env python3
# coding: utf-8
import datetime
from model.update_db import LogDatabase

class UpdateDatabase:

    def __init__(self):
        self.daily_date = datetime.date.today()
        self.db_update = LogDatabase()

    def update_database(self):
        """This method updates the database with modification identified in API response """
        # Si update_decision is True
        # Je récupère les ref des produits enregistrés dans un tableau
        # Je supprime la base produit et produits enregistrés
        # Je les recrées
        # Pour chaque catégorie dans la db:
            #je relance la procédure d'injection produit présent dans db creation sa race (a initier dans __init__)
        # Pour chaque produits enregistrés dans la liste:
            #s'il est présent dans la table produit:
                #je le réinjecte avec le statut Disponible
            #sinon, je le réinjecte avec le statut plus disponible

        pass

    def update_decision(self):
        """ This method decides if an update of the database has to be done """
        last_update_date = self.db_update.get_last_update_date() #type: datetime.date
        duration = self.daily_date - last_update_date #type: datetime.timedelta

        if duration.days >= 7:
            return True

#! /usr/bin/env python3
# coding: utf-8
from .dbconnexion import SQLconnexion

class UpdateDatabase:

    def __init__(self):
        pass

    def create_db(self):
        """ This method creates the database to manage the update """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = "DROP TABLE IF EXISTS Database_update"
                cursor.execute(sql)

            with connexion.cursor() as cursor:
                sql = "CREATE TABLE Database_update ( \
                    id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
                    update_date DATE NOT NULL, \
                    PRIMARY KEY (id) \
                    ) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4"
                cursor.execute(sql)

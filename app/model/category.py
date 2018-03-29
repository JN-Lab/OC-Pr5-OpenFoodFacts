#! /usr/bin/env python3
# coding: utf-8
from .dbconnexion import SQLconnexion

class Category:

    def __init__(self):
        pass

    def create_category_db(self):
        """ This method creates the product database """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = "DROP TABLE IF EXISTS Category"
                cursor.execute(sql)

            with connexion.cursor() as cursor:
                sql = "CREATE TABLE Category ( \
                    id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT, \
                    category_name VARCHAR(70) NOT NULL, \
                    category_product_number SMALLINT UNSIGNED, \
                    PRIMARY KEY (id) \
                    ) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4"
                cursor.execute(sql)

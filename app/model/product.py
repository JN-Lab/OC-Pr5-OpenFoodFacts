#! /usr/bin/env python3
# coding: utf-8
from .dbconnexion import SQLconnexion

class Product:

    def __init__(self):
        pass

    def create_product_db(self):
        """ This method creates the product database """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = "DROP TABLE IF EXISTS Product"
                cursor.execute(sql)

            with connexion.cursor() as cursor:
                sql = "CREATE TABLE Product ( \
                    id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
                    product_name VARCHAR(200) NOT NULL, \
                    product_sku BIGINT UNSIGNED NOT NULL, \
                    product_description TEXT, \
                    store VARCHAR(200), \
                    website_link VARCHAR(250), \
                    nutriscore CHAR(1) NOT NULL, \
                    category_id TINYINT UNSIGNED NOT NULL, \
                    PRIMARY KEY (id) \
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"
                cursor.execute(sql)

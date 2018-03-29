#! /usr/bin/env python3
# coding: utf-8
from .dbconnexion import SQLconnexion

class ProductDatabase:

    def __init__(self):
        pass

    def create_db(self):
        """ This method creates the product database """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = "DROP TABLE IF EXISTS Product"
                cursor.execute(sql)

            with connexion.cursor() as cursor:
                sql = """CREATE TABLE Product (
                    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                    product_name VARCHAR(200) NOT NULL,
                    product_sku BIGINT UNSIGNED NOT NULL,
                    product_description TEXT,
                    store VARCHAR(200),
                    website_link VARCHAR(250),
                    nutriscore CHAR(1) NOT NULL,
                    category_id TINYINT UNSIGNED NOT NULL,
                    PRIMARY KEY (id)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"""
                cursor.execute(sql)

    def inject_product(self, product, category_name):
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = """INSERT INTO Product
                    (product_name, product_sku, product_description, store, website_link, nutriscore, category_id)
                    SELECT %s, %s, %s, %s, %s, %s, id AS cat_id
                    FROM Category WHERE category_name = %s"""
                cursor.execute(sql, (product['name'], product['ref'], product['description'], product['store'], product['url'], product['score'], category_name))
            connexion.commit()

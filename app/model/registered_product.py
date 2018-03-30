#! /usr/bin/env python3
# coding: utf-8
from .dbconnexion import SQLconnexion

class RegisteredProductDatabase:

    def __init__(self):
        pass

    def create_db(self):
        """ This method creates the database to save products """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = "DROP TABLE IF EXISTS Product_registered"
                cursor.execute(sql)

            with connexion.cursor() as cursor:
                sql = """CREATE TABLE Product_registered (
                    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                    product_id INT UNSIGNED NOT NULL,
                    registered_date DATE NOT NULL,
                    PRIMARY KEY (id)
                    ) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4"""
                cursor.execute(sql)

    def create_keys(self):
        """ This method creates the necessary keys """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = """ALTER TABLE Product_registered
                    ADD CONSTRAINT fk_product_registered_product_id
                    FOREIGN KEY (product_id)
                    REFERENCES Product (id) ON DELETE CASCADE"""
                cursor.execute(sql)

    def get_product_ref(self):
        """ This method gets the product sku from the product registered """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = """SELECT product_sku FROM Product
                    WHERE id IN
                        (SELECT product_id
                        FROM Product_registered)"""
                cursor.execute(sql)
                result = cursor.fetchall()
                return result

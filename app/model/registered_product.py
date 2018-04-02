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
                    product_availability VARCHAR(15) NOT NULL,
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

    def get_products_ref(self):
        """ This method gets the product sku from the product registered """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                products_ref = []
                sql = """SELECT product_sku FROM Product
                    WHERE id IN
                        (SELECT product_id
                        FROM Product_registered)"""
                rows = cursor.execute(sql)
                for row in range(rows):
                    product_ref = cursor.fetchone()
                    products_ref.append(product_ref[0])
                return products_ref

    def inject_product(self, product_ref, availability):
        """ This method injects a product with its availability
        availability arg can only have two values : 'disponible'
        or 'indisponible' """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = """INSERT INTO Product_registered
                        (product_id, product_availability)
                    SELECT id AS pr_id, %s
                    FROM Product WHERE %s = Product.product_sku """
            cursor.execute(sql, (availability, product_ref))
        connexion.commit()

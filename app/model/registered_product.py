#! /usr/bin/env python3
# coding: utf-8
from .dbconnexion import SQLconnexion

class RegisteredProductDatabase:
    """ This class groups all the necessary SQL request linked to the
    Product_registered table """

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

    def get_product_from_ref(self, product_ref):
        """ This method get (if saved) the product id from Product_registered
        database"""
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = """SELECT product_id FROM Product_registered
                    INNER JOIN Product
                        ON Product_registered.product_id = Product.id
                    WHERE Product.product_sku = %s"""
                cursor.execute(sql, (product_ref))
                result = cursor.fetchone()
                return result

    def get_all_products_saved(self):
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = """SELECT product_name, product_description, store,
                                website_link, nutriscore, product_sku,
                                product_availability
                    FROM Product
                    INNER JOIN Product_registered
                        ON Product.id = Product_registered.product_id
                    WHERE Product_registered.product_id IS NOT NULL"""
                cursor.execute(sql)
                result = cursor.fetchall()
                return result

    def inject_product(self, product_ref, availability):
        """ This method injects a product with its availability
        availability arg can only have two values : 'disponible'
        or 'indisponible' """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = """INSERT INTO Product_registered
                        (product_id, product_availability)
                    SELECT Product.id, %s
                    FROM Product WHERE Product.product_sku = %s"""
                cursor.execute(sql, (availability, product_ref))
            connexion.commit()

#! /usr/bin/env python3
# coding: utf-8
from .dbconnexion import SQLconnexion

class CategoryDatabase:

    def __init__(self):
        pass

    def create_db(self):
        """ This method creates the category database """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = "DROP TABLE IF EXISTS Category"
                cursor.execute(sql)

            with connexion.cursor() as cursor:
                sql = """CREATE TABLE Category (
                    id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
                    category_name VARCHAR(70) NOT NULL,
                    PRIMARY KEY (id)
                    ) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4"""
                cursor.execute(sql)

    def inject_categories(self, category_list):
        """ This method injects the categories from a list """

        with SQLconnexion() as connexion:
            for category in category_list:
                with connexion.cursor() as cursor:
                    sql = "INSERT INTO Category (category_name) VALUES (%s)"
                    cursor.execute(sql, (category))
                connexion.commit()

    def get_categories(self):
        """ This method gets the categories selected for the app """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = "SELECT category_name FROM Category"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result

#! /usr/bin/env python3
# coding: utf-8
from .dbconnexion import SQLconnexion

class LogDatabase:

    def __init__(self):
        pass

    def create_db(self):
        """ This method creates the database to manage the update """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = "DROP TABLE IF EXISTS Database_update"
                cursor.execute(sql)

            with connexion.cursor() as cursor:
                sql = """CREATE TABLE Database_update (
                    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                    update_date DATE NOT NULL,
                    PRIMARY KEY (id)
                    ) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4"""
                cursor.execute(sql)

    def inject_update_date(self):
        """ This method injects the date when an update is done """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = """INSERT INTO Database_update (update_date)
                    VALUES (CURDATE())"""
                cursor.execute(sql)
            connexion.commit()

    def get_last_update_date(self):
        """ This method gets the last update date and return a datetime.date """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = """SELECT update_date FROM Database_update
                    ORDER BY update_date DESC
                    LIMIT 1"""
                cursor.execute(sql)
                result = cursor.fetchone()
                return result[0]

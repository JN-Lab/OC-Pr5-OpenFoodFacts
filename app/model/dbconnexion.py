#! /usr/bin/env python3
# coding: utf-8

from .password import *
import pymysql

class SQLconnexion(object):
    """ Context Manager to deals with the SQL connexion to the database """

    def __init__(self):
        self.host = HOST
        self.username = USERNAME
        self.password = PASSWORD
        self.database = DATABASE
        self.connexion = None

    def __enter__(self):
        self.connexion = pymysql.connect(host=self.host, user=self.username, passwd=self.password, db=self.database, charset='utf8mb4')
        return self.connexion

    def __exit__(self, type, value, traceback):
        self.connexion.close()

#! /usr/bin/env python3
# coding: utf-8

import password as pw
import pymysql

class SQLconnexion(object):

    def __init__(self):
        self.host = pw.HOST
        self.username = pw.USERNAME
        self.password = pw.PASSWORD
        self.database = pw.DATABASE
        self.connexion = None

    def __enter__(self):
        self.connexion = pymysql.connect(host=self.host, user=self.username, passwd=self.password, db=self.database, charset='utf8mb4')
        return self.connexion

    def __exit__(self, type, value, traceback):
        self.connexion.close()

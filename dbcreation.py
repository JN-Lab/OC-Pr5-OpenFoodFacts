#! /usr/bin/env python3
# coding: utf-8

from contextlib import contextmanager
from math import ceil
import urllib.parse
import re

import requests
import pymysql

from dbconnexion import SQLconnexion
import constants as c

class DatabaseCreation:
    """ This class creates the database linked to the program """

    def __init__(self):
        self.categories = []

    def __get_search_url(self, category, page_size, page):
        """ This method creates the products url needed """

        suffixe_url_element = {
            'action' : 'process',
            'tagtype_0' : 'categories',
            'tag_contains_0' : 'contains',
            'tag_0' : category,
            'page_size' : page_size,
            'page' : page,
            'json' : '1'
        }
        prefixe_url = 'https://fr.openfoodfacts.org/cgi/search.pl?'

        return prefixe_url + urllib.parse.urlencode(suffixe_url_element)

    def prepare(self):
        """ This method prepares the database """

        self.__database_creation()
        self.__get_categories()
        self.__inject_categories()
        self.__feed_database()

    def __feed_database(self):
        """ This method feeds the database """

        page_size = 1000
        for category in self.categories:
            page_number = self.__get_product_pages_number(category, str(page_size))
            for page in range(1, page_number + 1, 1):
                data = self.__get_product_page(category, str(page_size), str(page))
                print('page produit récupérées')
                self.__inject_products_page(data['products'], category['name'])

    def __get_product_pages_number(self, category, products_per_page):
        """ This method gets the necessary page number to request for a category """

        url = self.__get_search_url(category['name'], '20', '1')

        request = requests.get(url)
        data = request.json()

        page_number = ceil(int(data['count']) / int(products_per_page))

        return page_number

    def __get_product_page(self, category, page_size, page):
        """ This method gets the json linked to a specific page """

        url = self.__get_search_url(category['name'], page_size, page)

        request = requests.get(url)
        return request.json()

    def __inject_products_page(self, data, category_name):
        """ This method injects all the products from a page """

        print("Injection des produits de la catégorie {}".format(category_name))
        for product in data:
            product_info = self.__get_product_information(product)
            if product_info['injection']:
                self.__inject_product(product_info, category_name)

    def __get_product_information(self, product):
        """ This method cleans and get the needed product informations """

        product_info = {
            'injection' : True,
            'url' : '',
            'score' : '',
            'name' :'',
            'ref' : '',
            'store' : '',
            'description' : ''
        }

        try:
            product_info['url'] = product['url']
        except KeyError:
            product_info['url'] = 'NULL'

        try:
            product_info['score'] = product['nutrition_grade_fr']
        except KeyError:
            product_info['score'] = 'NULL'
            product_info['injection'] = False

        try:
            product_info['name'] = product['product_name_fr']
        except KeyError:
            product_info['name'] = 'NULL'
            product_info['injection'] = False

        try:
            product_info['ref'] = product['code']
        except KeyError:
            product_info['ref'] = 'NULL'
            product_info['injection'] = False

        try:
            product_info['store'] = product['stores']
        except KeyError:
            product_info['store'] = 'NULL'

        try:
            product_info['description'] = product['generic_name_fr']
        except KeyError:
            product_info['description'] = 'NULL'

        return product_info

    def __inject_product(self, product, category_name):

        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = "INSERT INTO Product (product_name, product_sku, product_description, store, website_link, nutriscore, category_id) \
                    SELECT %s, %s, %s, %s, %s, %s, id AS cat_id \
                    FROM Category WHERE category_name = %s"
                cursor.execute(sql, (product['name'], product['ref'], product['description'], product['store'], product['url'], product['score'], category_name))
            connexion.commit()

    def __inject_categories(self):
        """ This method injects in the database the categories selected """

        with SQLconnexion() as connexion:
            for category in self.categories:
                with connexion.cursor() as cursor:
                    sql = "INSERT INTO Category (category_name, category_product_number) VALUES (%s, %s)"
                    cursor.execute(sql, (category['name'], category['product_numb']))
                connexion.commit()


    def __get_categories(self):
        """ This method aims at getting the categories from openfoodfacts API to
        inject in database  """

        print("DEBUT : recherche de catégories pertinentes")

        url = 'https://fr.openfoodfacts.org/categories&json=1'

        request = requests.get(url)
        data = request.json()

        category_added = 0

        for category_info in data['tags']:
            if category_added < c.MAX_CATEGORY:
                match = re.search(r'categorie\/(.*)', category_info['url'])
                category = match.group(1)
                product_numb = category_info['products']
                pertinence = self.__analyze_category_pertinence(category, product_numb)
                if pertinence:
                    self.categories.append({'name': category, 'product_numb' : product_numb})
                    category_added += 1
            else:
                break

        print("FIN : Les {} categories ont été sélectionnées".format(c.MAX_CATEGORY))

    def __analyze_category_pertinence(self, category, product_numb):
        """ This method find 4 pertinent categories by analyzing the repartion of
        nutrition grade on a sample of 100 products """

        print("analyse de la pertinence de {}".format(category))

        # Look for a category with more than 1000 and less than 5000
        if product_numb > c.MIN_PRODUCT_NUMB and product_numb < c.MAX_PRODUCT_NUMB:
            sample = 100
            final_product_sample = 100
            url = self.__get_search_url(category, sample, '1')

            request = requests.get(url)
            data = request.json()

            score_list = [0, 0, 0, 0, 0]

            # We analyze the repartition of nutrition grade
            for product in data['products']:
                try:
                    score_grade = product['nutrition_grade_fr']
                    if score_grade == 'a':
                        score_list[0] += 1
                    elif score_grade == 'b':
                        score_list[1] += 1
                    elif score_grade == 'c':
                        score_list[2] += 1
                    elif score_grade == 'd':
                        score_list[3] += 1
                    elif score_grade == 'e':
                        score_list[4] += 1
                except:
                    final_product_sample -= 1

            # We check the pertinence of the category according its repartition by nutrition_grade
            if final_product_sample > sample / 2:
                number_match = []
                for score_numb in score_list:
                    min_required = score_numb / final_product_sample
                    if min_required >= 0.05:
                        number_match.append(min_required)

                print(number_match)

                if len(number_match) == 5:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


    def __database_creation(self):
        """ This method manages the creation of the database """

        print('DEBUT : Création de la base de données')

        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = "SET NAMES utf8mb4"
                cursor.execute(sql)
            connexion.commit()

            with connexion.cursor() as cursor:
                sql = "DROP TABLE IF EXISTS Product_registered"
                cursor.execute(sql)
            connexion.commit()

            with connexion.cursor() as cursor:
                sql = "DROP TABLE IF EXISTS Product"
                cursor.execute(sql)
            connexion.commit()

            with connexion.cursor() as cursor:
                sql = "DROP TABLE IF EXISTS Category"
                cursor.execute(sql)
            connexion.commit()

            with connexion.cursor() as cursor:
                sql = "DROP TABLE IF EXISTS Database_update"
                cursor.execute(sql)
            connexion.commit()

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
            connexion.commit()

            with connexion.cursor() as cursor:
                sql = "CREATE TABLE Category ( \
                    id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT, \
                    category_name VARCHAR(70) NOT NULL, \
                    category_product_number SMALLINT UNSIGNED, \
                    PRIMARY KEY (id) \
                    ) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4"
                cursor.execute(sql)
            connexion.commit()

            with connexion.cursor() as cursor:
                sql = "CREATE TABLE Product_registered ( \
                    id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
                    product_id INT UNSIGNED NOT NULL, \
                    registered_date DATE NOT NULL, \
                    PRIMARY KEY (id) \
                    ) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4"
                cursor.execute(sql)
            connexion.commit()

            with connexion.cursor() as cursor:
                sql = "CREATE TABLE Database_update ( \
                    id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
                    update_date DATE NOT NULL, \
                    PRIMARY KEY (id) \
                    ) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4"
                cursor.execute(sql)
            connexion.commit()

            with connexion.cursor() as cursor:
                sql = "ALTER TABLE Product_registered ADD CONSTRAINT fk_product_registered_product_id \
                    FOREIGN KEY (product_id) \
                    REFERENCES Product (id) ON DELETE CASCADE"
                cursor.execute(sql)
            connexion.commit()

        print('FIN : Base de données créées')

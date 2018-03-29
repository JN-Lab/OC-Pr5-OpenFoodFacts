#! /usr/bin/env python3
# coding: utf-8

import re
import urllib.parse
import requests
from .controller_constants import *

class OpenFoodFactsInteractions:

    def __init__(self):
        self.category_list = []

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

    def get_categories(self):
        """ This method aims at getting the categories from openfoodfacts API to
        inject in database  """

        print("DEBUT : recherche de catégories pertinentes")

        url = 'https://fr.openfoodfacts.org/categories&json=1'

        request = requests.get(url)
        data = request.json()

        category_added = 0

        for category_info in data['tags']:
            if category_added < MAX_CATEGORY:
                match = re.search(r'categorie\/(.*)', category_info['url'])
                category = match.group(1)
                product_numb = category_info['products']
                pertinence = self.__analyze_category_pertinence(category, product_numb)
                if pertinence:
                    self.category_list.append(category)
                    category_added += 1
            else:
                break

        print("FIN : Les {} categories ont été sélectionnées".format(MAX_CATEGORY))

    def __analyze_category_pertinence(self, category, product_numb):
        """ This method find 4 pertinent categories by analyzing the repartion of
        nutrition grade on a sample of 100 products """

        print("analyse de la pertinence de {}".format(category))

        # Look for a category with more than 1000 and less than 5000
        if product_numb > MIN_PRODUCT_NUMB and product_numb < MAX_PRODUCT_NUMB:
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

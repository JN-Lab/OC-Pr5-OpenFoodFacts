#! /usr/bin/env python3
# coding: utf-8
import math
import urllib.parse
import requests
from view.consoleapiview import ConsoleApiView

class OpenFoodFactsInteractions:

    def __init__(self):
        self.interface = ConsoleApiView()
        #Categories renseignées en dur 'pour le moment'
        self.category_list = ['sandwichs', 'barres', 'pizzas', 'biscuits-aperitifs']

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

    def get_product_pages_number(self, category, products_per_page):
        """ This method gets the necessary page number to request for a category """

        url = self.__get_search_url(category, '20', '1')

        request = requests.get(url)
        data = request.json()

        page_number = math.ceil(int(data['count']) / int(products_per_page))

        return page_number

    def get_product_page(self, category, page_size, page):
        """ This method gets the json linked to a specific page """

        url = self.__get_search_url(category, page_size, page)

        request = requests.get(url)
        return request.json()

import requests
import time
import os
import json


class Parser5ka:
    _domain = 'https://5ka.ru'
    _api_path = '/api/v2/special_offers/'
    _api_path_cat = '/api/v2/categories/'
    _url_category_part_1 = 'https://5ka.ru/api/v2/special_offers/?store=&categories='
    _url_category_part_2 = '&ordering=&price_promo__gte=&price_promo__lte=&search='

    params = {
        'records_per_page': 50
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
    }

    def __init__(self):
        self.products = []
        self.categories_prod = []

    def download(self):
        params = {}
        category_url = self._domain + self._api_path_cat
        categories = requests.get(category_url, headers=self.headers, params=params).json()
        for elem in categories:
            self.categories_prod.append(elem)
        for el in self.categories_prod:
            el.update({'products': []})
            parent_group_code = el['parent_group_code']

            url = self._url_category_part_1 + parent_group_code + self._url_category_part_2

            params = self.params
            response = requests.get(url, headers=self.headers, params=params)
            if response.headers['Content-Type'] == 'application/json':
                products = response.json()
                for product in products['results']:
                    el['products'].append(product)
                time.sleep(0.1)
            else:
                break

    def category_files(self):
        os.mkdir('category_files')
        for elem in self.categories_prod:
            parent_group_name = elem['parent_group_name']
            file_path = os.path.join('category_files', '{0}.json'.format(parent_group_name))
            with open(file_path, 'w', encoding='UTF-8') as file:
                json.dump(elem, file, ensure_ascii=False)


if __name__ == '__main__':
    parser = Parser5ka()
    parser.download()
    parser.category_files()
    print(1)



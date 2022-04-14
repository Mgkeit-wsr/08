from AbstractRequester import *

import json
import requests


class HHRequester(AbstractRequester):
    url = "https://api.hh.ru/vacancies"
    data = {}
    options = {}
    params = {
        'area': 1,  # Поиск ощуществляется по вакансиям города Москва
        'page': 0,  # Индекс страницы поиска на HH
        'per_page': 1  # Кол-во вакансий на 1 странице
    }

    def get_options(self, opt):
        self.options = opt

    def add_options(self):
        self.params.update(self.options)

    def send_jobs(self):
        # print(self.params)
        return AbstractRequester.request(self, self.url, self.params)

    def get_professional_roles_id(txt, self):
        tmp = AbstractRequester.request(self, 'https://api.hh.ru/suggests/professional_roles', 'text=' + txt)
        return json.loads(tmp)['items'][0]['id']

    def get_experience_id(self):
        tmp = AbstractRequester.request(self, 'https://api.hh.ru/dictionaries', 'text=experience')
        # ans = []
        # for i in range(4):
        #     ans.append(json.loads(tmp)['experience'][i]['id'])
        # return ans

        tmp = json.loads(tmp)
        ans = {}
        for i in tmp['experience']:
            ans[i['name'].lower()] = i['id']
        return ans

    def get_metro_id(self):
        tmp = AbstractRequester.request(self, 'https://api.hh.ru/metro/1', 'text=')
        tmp = json.loads(tmp)
        ans = {}
        for i in tmp['lines']:
            # print(i['stations'])
            for j in i['stations']:
                # print(j['name'], j['id'])
                ans[j['name'].lower()] = j['id']
        return ans

    def get_employment_id(self):
        tmp = AbstractRequester.request(self, 'https://api.hh.ru/dictionaries', 'text=')
        tmp = json.loads(tmp)
        ans = {}
        for i in tmp['employment']:
            ans[i['name'].lower()] = i['id']

        return ans

    def get_schedule_id(self):
        tmp = AbstractRequester.request(self, 'https://api.hh.ru/dictionaries', 'text=')
        tmp = json.loads(tmp)
        ans = {}
        for i in tmp['schedule']:
            ans[i['name'].lower()] = i['id']

        return ans

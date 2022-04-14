from abc import (
  ABC,
  abstractmethod,
)

import requests


class AbstractRequester:
    @property
    @abstractmethod
    def get_options(self):
        pass

    @abstractmethod
    def add_options(self):
        pass

    @staticmethod
    @abstractmethod
    def request(self, address, params):
        req = requests.get(address, params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
        req.close()
        # return json.loads(self.data)
        return data

    @abstractmethod
    def send_jobs(self):
        pass

    url = ""
    data = {}
    params = {}

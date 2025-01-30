from abc import ABC

import requests

from src.abstract_classes import BaseSaveFile, BaseLoadVacancies
from config import DATA_DIR

class Head_Hunter_API(BaseSaveFile, BaseLoadVacancies):
    """Получает информацию о вакансиях с HH"""

    def __init__(self, file_worker: str = "data/vacancies.json"):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword: str):
        """Метод загрузки данных вакансий"""
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

        return self.__vacancies


if __name__ == '__main__':
    hh = Head_Hunter_API(file_worker=DATA_DIR)
    hh.load_vacancies("Разработчик")

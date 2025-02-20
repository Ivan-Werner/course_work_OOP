import json
from abc import ABC

from src.vacancy import Vacancy
from src.abstracts import BaseSaver
from config import path_to_data_json

class JSONSaver(BaseSaver):
    def __init__(self, path_to_file=path_to_data_json):
        self.__path = path_to_file


    def save_to_file(self, vacancies):
        """Функция добавляет данные в JSON-файл"""
        vacancies_info = [vac.to_json() for vac in vacancies]
        with open(self.__path, "w", encoding="utf-8") as file:
            json.dump(vacancies_info, file, ensure_ascii=False, indent=4)


    def read_from_file(self):
        with open(self.__path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data


    def del_from_file(self):
        """Функция удаляет данные из файла"""
        with open(self.__path, "w"):
            pass





# class JSONSaver(BaseSaver):
#     def save_to_file(self, vacancies):
#         json.load()
#         json.dump()

#     def def_from_file(self, url):
#         pass
#
#     def filter_by_words(self, words_list):
#         pass


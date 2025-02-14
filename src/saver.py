import json
from abc import ABC

from src.vacancy import Vacancy
from src.abstracts import BaseSaver
from config import path_to_data_json

class JSONSaver(BaseSaver):
    def __init__(self):
        self.path = path_to_data_json

    def save_to_file(self, vacancies):
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False)





# class JSONSaver(BaseSaver):
#     def save_to_file(self, vacancies):
#         json.load()
#         json.dump()

#     def def_from_file(self, url):
#         pass
#
#     def filter_by_words(self, words_list):
#         pass


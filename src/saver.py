import json
from src.abstracts import BaseSaver
from config import path_to_data_json

class JSONSaver(BaseSaver):
    def __init__(self, path_to_file=path_to_data_json):
        self.__path = path_to_file


    def save_to_file(self, vacancies):
        """Функция добавляет данные в JSON-файл, исключая дубли"""
        try:
            with open(self.__path, "r", encoding="utf-8") as source_file:
                data = json.load(source_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        existing_vacancies = {vac["url"]: vac for vac in data}

        existing_vacancies.update({vac.url: vac.to_json() for vac in vacancies})

        with open(self.__path, "w", encoding="utf-8") as file:
            json.dump(list(existing_vacancies.values()), file, ensure_ascii=False, indent=4)



    def read_from_file(self):
        with open(self.__path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data


    def del_from_file(self):
        """Функция удаляет данные из файла"""
        with open(self.__path, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)







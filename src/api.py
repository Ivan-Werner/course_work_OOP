from src.abstracts import BaseAPI
import requests

class APIHeadHunter(BaseAPI):
    """Класс для запросов по API с HH"""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []


    def get_vacancies(self, keyword):
        """Получаем вакансии по API с ресурса HH.ru"""
        self.params["text"] = keyword
        response = requests.get(self.__url, params=self.params, headers=self.__headers)
        if response.status_code == 200:
            vacancies_info = response.json()["items"]
            return vacancies_info
        else:
            print(f"Ошибка соединения: {response.status_code}")
            return []

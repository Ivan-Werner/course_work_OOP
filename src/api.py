from src.abstracts import BaseAPI
import requests

class HHAPI(BaseAPI):
    """Класс для парсинга данных по вакансиям"""
    city: str
    area: int
    page: int
    vacancy: str
    params: dict

    url = "https://api.hh.ru/vacancies"

    def __init__(self, city, number_of_city, page, vacancy):
        self.city = city
        self.number_of_city = number_of_city
        self.page = page
        self.vacancy = vacancy
        self.params = self.get_params()

    def get_params(self):
        params = {
            'text': f"{self.vacancy} {self.city}",
            'area': 1,
            'specialization': {self.number_of_city},
            'per_page' : 100,
            'page' : self.page
        }
        return params

    @classmethod
    def get_url(cls):
        return cls.url

    def parsing_data(self):
        response = requests.get(url=self.get_url(), params=self.params)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Request failed with status code: {response.status_code}"


hh_vacancies = HHAPI('Москва', 1, 1, 'Повар')
hh_vacancies.get_params()
data_set_vacancies = hh_vacancies.parsing_data()
print(data_set_vacancies)
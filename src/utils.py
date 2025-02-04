from src.vacancy import Vacancy


def user_interaction():
    api = HHApi()
    word = input()
    vacancies_info = api.get_vacancies(word)
    vacancies = Vacancy.cast_to_objects(vacancies_info)

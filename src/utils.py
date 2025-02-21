from src.api import APIHeadHunter
from src.saver import JSONSaver
from src.vacancy import Vacancy
import re

def top_vacancy(number, vacancies_list):
    """Функция определения Топа вакансий"""
    if number == "":
        return vacancies_list
    else:
        return vacancies_list[0:int(number)]


def filter_words(main_list, pattern):
    """Поиск вакансий по ключевым словам в разделе Требования"""
    res = []
    for i in main_list:
        if pattern in i["requirements"]:
            res.append(i)
    return res



def user_interaction():
    vacancy_parser= APIHeadHunter()
    vacancy_name = input("Введите название вакансии: ")
    vacancies_data = vacancy_parser.get_vacancies(vacancy_name)
    vacancies = Vacancy.cast_to_objects(vacancies_data)
    saver = JSONSaver()
    saver.save_to_file(vacancies)
    vacancies_dicts = saver.read_from_file()
    vacancies_list = []
    for vacancy in vacancies_dicts:
        vacancies_list.append(Vacancy(**vacancy))
    sorted_list = sorted(vacancies_list, reverse=True)
    """Топ записей"""
    top_n = input("Введите сколько Топ-вакансий вы хотите посмотреть: ")
    res = top_vacancy(top_n, sorted_list)
    for i in res:
        print(i["requirements"])



if __name__ == '__main__':
    user_interaction()

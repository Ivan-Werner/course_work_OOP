from src.vacancy import Vacancy

def top_vacancy(number, vacancies_list):
    """Функция определения Топа вакансий"""
    if number == "":
        return vacancies_list
    else:
        return vacancies_list[0:int(number)]


def filter_words():
    """Поиск вакансий по ключевым словам"""
    pass




def user_interaction():
    pass

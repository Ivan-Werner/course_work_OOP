from src.vacancy import Vacancy

def top_vacancy(number, vacancies_list):
    """Функция определения Топа вакансий"""
    if number == "":
        return vacancies_list
    else:
        return vacancies_list[0:int(number)]


def filter_words(res_list, words_list):
    """Поиск вакансий по ключевым словам"""
    result_list = []
    for index in res_list:
        for i in words_list:
            if index["requirements"] is None:
                continue
            elif i in index["requirements"] or i in index["name"]:
                result_list.append(index)
    return result_list




def user_interaction():
    pass

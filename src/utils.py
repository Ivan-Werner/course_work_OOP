from src.api import APIHeadHunter
from src.saver import JSONSaver
from src.vacancy import Vacancy


def top_vacancy(number, vacancies_list):
    """Функция определения Топа вакансий"""
    if number == "":
        return vacancies_list
    else:
        return vacancies_list[0:int(number)]


def filter_city(main_vacancies_list, pattern_city="Москва"):
    """Поиск вакансий по полю Город"""
    vacancies_on_city = []
    for vac in main_vacancies_list:
        if vac.city.lower() == pattern_city.lower():
            vacancies_on_city.append(vac)
    return vacancies_on_city





def user_interaction():
    vacancy_parser= APIHeadHunter()
    vacancy_name = input("Введите название вакансии, которую вы хотите добавить в файл: ")
    # city_choised = input("Выберете город, в котором ищете вакансии: ")




    vacancies_data = vacancy_parser.get_vacancies(vacancy_name)
    vacancies = Vacancy.cast_to_objects(vacancies_data)
    saver = JSONSaver()
    saver.save_to_file(vacancies)
    vacancies_dicts = saver.read_from_file()
    vacancies_list = []
    for vacancy in vacancies_dicts:
        vacancies_list.append(Vacancy(**vacancy))
    # print(vacancies_list)

    city_choised = input("Хотите ли выбрать город для фильтрации (да / нет): ").lower()


    if city_choised == "да":
        print("Введите название города. По умолчанию - Москва: ")
        city_name = input()
        vacancies_list = filter_city(vacancies_list, city_name)
    elif city_choised == "нет":
        vacancies_list = filter_city(vacancies_list)



    # vacancies_list = filter_city(vacancies_list, city_choised)
    # print(vacancies_list)

    top_n = input("3. Выберете Топ-n вакансий по заработной плате (введите n).\n"
                  "Нажмите Enter, для вывода всего списка:\n ")
    sorted_list = sorted(vacancies_list, reverse=True)
    """Топ записей"""


    res = top_vacancy(top_n, sorted_list)
    for i in res:
        print(i)

    del_data = input("Удалить данные их файла? (да / нет): ").lower()
    if del_data == "да":
        saver.del_from_file()
        print("Файл очищен.")
    else:
        print("Данные сохранены в файл.")






if __name__ == '__main__':
    user_interaction()

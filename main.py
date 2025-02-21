from src.utils import user_interaction, top_vacancy
from src.api import APIHeadHunter
from src.saver import JSONSaver
from src.vacancy import Vacancy


if __name__ == '__main__':
    """Запрос данных по API и запись в JSON-файл"""
    vacancy_parser= APIHeadHunter()
    vacancies_data = vacancy_parser.get_vacancies("юрист")
    vacancies = Vacancy.cast_to_objects(vacancies_data)
    saver = JSONSaver()
    saver.save_to_file(vacancies)
    vacancies_dicts = saver.read_from_file()
    # print(res)
    # vacancy_name = input("Введите название вакансии: ")
    # vacancy_parser = APIHeadHunter()
    # vacancies_data = vacancy_parser.get_vacancies(vacancy_name)
    # vacancies = Vacancy.cast_to_objects(vacancies_data)
    # saver = JSONSaver()
    # saver.save_to_file(vacancies)
    """Создание списка объектов класса и сортировка"""
    vacancies_list = []
    for vacancy in vacancies_dicts:
        vacancies_list.append(Vacancy(**vacancy))
    # print(vacancies_list)
    sorted_list = sorted(vacancies_list, reverse=True)
    """Топ записей"""
    res = top_vacancy(5, sorted_list)
    for i in res:
        print(i)

    """Удаление данных из файла"""
    # saver.del_from_file()



    # del_q = input("Удалить данные из файла? y/n\n")
    # if del_q == "y":
    #     saver.del_from_file()



    # res_1 = Vacancy("крановщик","Москва", "водительского", 100000, 150000, "hh.ru")
    # res_2 = Vacancy("крановщик", "Иркутск", "водительского", 80000, 180000, "hh.ru")
    # res_3 = Vacancy("крановщик", "Москва", "водительского", 80000, 90000, "hh.ru")
    # vacancies = [res_1, res_2, res_3]
    # sorted_list = sorted(vacancies, reverse=True)
    # print(sorted_list)

    pass






# def main():
#     user_interaction()
#
#
# if __name__ == '__main__':
#     main()
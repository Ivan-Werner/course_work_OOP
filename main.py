from src.utils import user_interaction
from src.api import APIHeadHunter, hh_vacancies
from src.saver import JSONSaver
from src.vacancy import Vacancy

if __name__ == '__main__':
    vacancies_from_hh = APIHeadHunter()
    res = Vacancy("крановщик","Москва", "водительского", 100000, "hh.ru")
    print(res)




# def main():
#     user_interaction()
#
#
# if __name__ == '__main__':
#     main()
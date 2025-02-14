


class Vacancy:
    """Класс для работы с вакансиями"""
    # __slots__ = ("name", "city", "requirements", "salary", "url")

    def __init__(self, name, city, requirements, salary, url):
        self.name = name
        self.city = city
        self.requirements = requirements
        self.salary = salary
        self.url = url
        self.result = []


    @classmethod
    def cast_to_objects(cls, vacancies_info: list[dict]):
        all_vacancies = []
        for vac_info in vacancies_info:
            name = vac_info["name"]
            city = vac_info["area"]["name"]
            requirements = vac_info["snippet"] if vac_info["snippet"].get("requirement") else "Не указано"
            salary = vac_info["salary"]
            if salary:
                salary_from = salary["from"] if salary.get("from") else 0
                salary_to = salary["to"] if salary.get("to") else 0
            else:
                salary_from = 0
                salary_to = 0
            url = vac_info["alternate_url"]
            result = cls(name, city, requirements, salary, url)
            all_vacancies.append(result)
        return all_vacancies

    def filter_city(self):
        result_city = []
        for i in self.result:
            if self.city == i["city"]:
                result_city.append(i)
        return result_city

    def __le__(self, other, res_list):
        res_salary = []
        for i in res_list:
            if other <= i["salary"]["from"]:
                res_salary.append(i)
        return res_salary








# class Vacancy:
#     @classmethod
#     def cast_to_objects(cls, vacancies_info: list[dict]):
#         all_vacancies = []
#         for vac_info in vacancies_info:
#             title = vac_info['name']
#             city = vac_info['area']['name']
#             requirements = vac_info['snippet'] if vac_info['snippet'].get('requirements') else 'Не указано'
#             salary = vac_info['salary']
#             if salary:
#                 salary_from = salary['from'] if salary.get('from') else 0
#                 salary_to = salary['to'] if salary.get('to') else 0
#             else:
#                 salary_from = 0
#                 salary_to = 0
#
#             url = vac_info['alternate_url']
#             instance = cls(title, city, requirements, salary, url)
#             all_vacancies.append(instance)
#         return all_vacancies
#
#
#     def to_json(self):
#         pass




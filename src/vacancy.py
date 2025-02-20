


class Vacancy:
    """Класс для работы с вакансиями"""
    __slots__ = ("name", "city", "requirements", "salary_from", "salary_to", "url")

    def __init__(self, name, city, requirements, salary_from, salary_to, url):
        self.name = name
        self.city = city
        self.requirements = requirements
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url
        # self.result = []


    @classmethod
    def cast_to_objects(cls, vacancies_info: list[dict]):
        all_vacancies = []
        for vac_info in vacancies_info:
            name = vac_info["name"]
            city = vac_info["area"]["name"]
            requirements = vac_info["snippet"]["requirement"] if vac_info["snippet"].get("requirement") else "Не указано"
            salary = vac_info["salary"]
            if salary:
                salary_from = salary["from"] if salary.get("from") else 0
                salary_to = salary["to"] if salary.get("to") else 0
            else:
                salary_from = 0
                salary_to = 0
            url = vac_info["alternate_url"]
            result = cls(name, city, requirements, salary_from, salary_to, url)
            all_vacancies.append(result)
        return all_vacancies

    def to_json(self):
        return {"name": self.name, "city": self.city, "requirements": self.requirements,
                "salary_from": self.salary_from, "salary_to": self.salary_to, "url": self.url}

    # def filter_city(self):
    #     result_city = []
    #     for i in self.result:
    #         if self.city == i["city"]:
    #             result_city.append(i)
    #     return result_city

    def __lt__(self, other):
        # return self.salary_from < other.salary_from
        return (self.salary_from, self.salary_to) < (other.salary_from, other.salary_to)

    def __str__(self):
        return (f"Вакансия: {self.name}\nГород: {self.city}\nТребования: {self.requirements}\n"
                f"Зарплата от {self.salary_from} до {self.salary_to}\nURL: {self.url}\n")

    def __repr__(self):
        return f"{self.__class__.__name__}, зп {self.salary_from}"













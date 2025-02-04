

class Vacancy:
    @classmethod
    def cast_to_objects(cls, vacancies_info: list[dict]):
        all_vacancies = []
        for vac_info in vacancies_info:
            title = vac_info['name']
            city = vac_info['area']['name']
            requirements = vac_info['snippet'] if vac_info['snippet'].get('requirements') else 'Не указано'
            salary = vac_info['salary']
            if salary:
                salary_from = salary['from'] if salary.get('from') else 0
                salary_to = salary['to'] if salary.get('to') else 0
            else:
                salary_from = 0
                salary_to = 0

            url = vac_info['alternate_url']
            instance = cls(title, city, requirements, salary, url)
            all_vacancies.append(instance)
        return all_vacancies


    def to_json(self):
        pass




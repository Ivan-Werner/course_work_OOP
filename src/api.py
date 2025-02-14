from src.abstracts import BaseAPI
import requests

class APIHeadHunter(BaseAPI):


    # url = "https://api.hh.ru/vacancies"

    def __init__(self):
        self._url = "https://api.hh.ru/vacancies"
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []


    def get_vacancies(self, keyword):
        global vacancies
        self.params["text"] = keyword
        while self.params.get("page") != 20:
            response = requests.get(self._url, headers=self._headers, params=self.params)
            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.params["page"] += 1
        return vacancies

hh_vacancies = APIHeadHunter()

res = APIHeadHunter.get_vacancies(hh_vacancies, "крановщик")

# source_list = []
# for i in res:
#     attributes = {}
#     # print(i)
#     attributes["name"] = i["name"]
#     attributes["city"] = i["area"]["name"]
#     attributes["requirement"] = i["snippet"]["requirement"]
#     if i["salary"] is not None:
#         attributes["salary_from"] = i["salary"]["from"] if i["salary"].get("from") else 0
#         attributes["salary_to"] = i["salary"]["to"] if i["salary"].get("to") else 0
#     else:
#         attributes["salary_from"] = 0
#         attributes["salary_to"] = 0
#     # attributes["salary"] = i["salary"]
#     attributes["url"] = i["alternate_url"]
#     source_list.append(attributes)
# for i in source_list:
#     print(i)







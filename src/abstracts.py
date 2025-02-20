from abc import ABC, abstractmethod

class BaseAPI(ABC):
    """Абстрактный класс для API-запроса"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        """Метод отправки get-запроса на HeadHunter"""
        pass



class BaseSaver(ABC):
    @abstractmethod
    def save_to_file(self, vacancy_list):
        pass

    def del_from_file(self):
        pass

    # @abstractmethod
    # def def_from_file(self, del_keywords):
    #     pass

    # @abstractmethod
    # def filter_by_words(self, words_list):
    #     pass





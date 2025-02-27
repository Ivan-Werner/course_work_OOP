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
    """Абстрактный класс для работы с файлом"""
    @abstractmethod
    def save_to_file(self, vacancy_list):
        """Метод сохранения данных в файл"""
        pass

    def del_from_file(self):
        """Метод удаления данных из файла"""
        pass







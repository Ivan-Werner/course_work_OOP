from abc import ABC, abstractmethod


class BaseSaveFile(ABC):
    """Абстрактный класс инициализации пути до файлу"""

    @abstractmethod
    def __init__(self, file_worker):
        self.file_hh = file_worker


class BaseLoadVacancies(ABC):
    """Абстрактный класс для создания метода получения вакансий по ключевому слову"""

    @abstractmethod
    def load_vacancies(self, keyword):
        pass

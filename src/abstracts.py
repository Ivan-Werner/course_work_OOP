from abc import ABC, abstractmethod

class BaseSaver(ABC):
    @abstractmethod
    def save_to_file(self, vacancy):
        pass

    @abstractmethod
    def def_from_file(self, url):
        pass

    @abstractmethod
    def filter_by_words(self, words_list):
        pass

class BaseAPI(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_params(self):
        pass



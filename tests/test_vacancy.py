import unittest
from xml.dom.minidom import NamedNodeMap

from src.vacancy import Vacancy
from tests.conftest import vacancy


class TestVacancy(unittest.TestCase):
    def test_init(self):
        """тестируем инициализацию класса"""
        vacancy_test = Vacancy("Работник",
                               "Москва",
                               "Работать",
                               1000,
                               5000,
                               "https://example.com")

        self.assertEqual(vacancy_test.name, "Работник")
        self.assertEqual(vacancy_test.city, "Москва")
        self.assertEqual(vacancy_test.requirements, "Работать")
        self.assertEqual(vacancy_test.salary_from, 1000)
        self.assertEqual(vacancy_test.salary_to, 5000)
        self.assertEqual(vacancy_test.url, "https://example.com")






    def test_lt(self):
        """Тестируем сравнение по зп с помощью магического метода lt"""
        salary_from_1 = 1000
        salary_from_2 = 4000
        vacancy_test_1 = Vacancy(name="Работник",
                                 city="Москва",
                                 requirements="Работать",
                                 salary_from=salary_from_1,
                                 salary_to=0,
                                 url="https://example1.com")
        vacancy_test_2 = Vacancy(name="Работник покруче",
                                 city="Москва",
                                 requirements="Работать больше",
                                 salary_from=salary_from_2,
                                 salary_to=0,
                                 url="https://example2.com")
        self.assertTrue(vacancy_test_1 < vacancy_test_2)
        self.assertFalse(vacancy_test_2 < vacancy_test_1)


    def test_str(self):
        """Тестируем "красивый" вывод"""
        salary_from = 1000
        salary_to = 5000
        vacancy_test = Vacancy(name="Работник",
                               city="Москва",
                               requirements="Работать",
                               salary_from=salary_from,
                               salary_to=salary_to,
                               url="https://example.com")
        expected_input = ('Вакансия: Работник\n'
                          'Город: Москва\n'
                          'Требования: Работать\n'
                          'Зарплата от 1000 до 5000\n'
                          'URL: https://example.com\n')
        self.assertEqual(str(vacancy_test), expected_input)





if __name__ == '__main__':
    unittest.main()







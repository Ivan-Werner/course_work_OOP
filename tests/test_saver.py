import unittest
from unittest.mock import mock_open, patch
import json
import pytest

from coverage.html import read_data

from src.saver import JSONSaver
from src.vacancy import Vacancy
from tests.conftest import vacancy


class TestJSONSaver(unittest.TestCase):
    def setUp(self):
        self.path = "test_data.json"
        self.save_to_file = JSONSaver(self.path)

    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps({
        'items': [
            {
                'name': 'Должность',
                'city': 'Москва',
                'requirements': 'Работать',
                'salary_from': 1000,
                'salary_to': 5000,
                'url': 'https://example.com/apply'
            }
        ]
    }))

    def test_read_from_file(self, mock_file):
        self.save_to_file.read_from_file()
        self.assertEqual(len(self.save_to_file.read_from_file()), 1)


    def test_del_from_file(self):
        self.assertEqual(self.save_to_file.del_from_file(), None)

if __name__ == '__main__':
    unittest.main()

def test_json_existing_file(tmp_path):
    saver = JSONSaver(tmp_path / 'test.json')
    existing_vacancy_data = {
        'name': 'fake name',
        'city': 'some city',
        'requirements': 'req',
        'salary_from': 1,
        'salary_to': 100,
        'url': 'https://hh.ru/some/vac_1/'
    }

    with open(tmp_path / 'test.json', mode='w') as f:
        json.dump([existing_vacancy_data], f)
    new_vacancy_data = {
        'name': 'fake name',
        'city': 'some city',
        'requirements': 'req',
        'salary_from': 1,
        'salary_to': 100,
        'url': 'https://hh.ru/some/vac_2/'
    }
    vacancy = Vacancy(**new_vacancy_data)
    saver.save_to_file([vacancy])

    with open(tmp_path / 'test.json') as f:
        data = json.load(f)

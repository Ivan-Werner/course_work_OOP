import unittest
from unittest.mock import mock_open, patch
import json

from coverage.html import read_data

from src.saver import JSONSaver


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
        # self.assertEqual(self.save_to_file.read_from_file()[0], 'Должность')

    def test_del_from_file(self):
        self.assertEqual(self.save_to_file.del_from_file(), None)

if __name__ == '__main__':
    unittest.main()


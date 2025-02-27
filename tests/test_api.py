import unittest
from unittest.mock import MagicMock, patch
from src.api import APIHeadHunter

# class TestAPIHeadHunter(unittest.TestCase):
#     @patch('request.get')
#     def test_get_vacancies_error(self, mock_get):
#         mock_response = MagicMock()
#         mock_response.json.return_value = {
#             'items': [
#                 {'name': 'Developer', 'salary': 1500},
#                 {'name': 'QA', 'salary': 1000}
#             ]
#         }
#         mock_get.return_value = mock_response
#         hh = APIHeadHunter()
#         hh.get_vacancies('Developer')
#         self.assertGreater(len(hh.vacancies), 0)
#         self.assertEqual(hh.vacancies[0]['name'], 'Developer')
#         mock_get.assert_called_with(
#
#         )
#
#
# if __name__ == '__main__':
#     unittest.main()
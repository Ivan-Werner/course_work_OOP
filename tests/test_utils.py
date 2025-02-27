from src.utils import top_vacancy, filter_city
from src.vacancy import Vacancy
import pytest


def test_top_vacancy():
    assert top_vacancy(number= "", vacancies_list=[1, 2, 3]) == [1, 2, 3]
    assert top_vacancy(number=2, vacancies_list=[1, 2, 3]) == [1, 2]


def test_filter_city_empty():
    assert filter_city(main_vacancies_list=[]) == []


def _create_vacancy(**kwargs):
    data = {
        'name': 'fake name',
        'city': 'some city',
        'requirements': 'req',
        'salary_from': 1,
        'salary_to': 100,
        'url': 'https://hh.ru/some/vac/'
    }
    data.update(kwargs)
    return Vacancy(**data)

@pytest.mark.parametrize(
    ('search_city', 'vacancies_count'),
    [
        ('Moscow', 2),
        ('St. Petersburg', 1),
        ('Minsk', 0)
    ]
)
def test_filter_city(search_city, vacancies_count):
    vacancies = [
        _create_vacancy(city='Moscow'),
        _create_vacancy(city='Moscow'),
        _create_vacancy(city='St. Petersburg'),
        _create_vacancy(city='Sochi')
    ]

    filtered_vacancies = filter_city(vacancies, pattern_city=search_city)
    assert len(filtered_vacancies) == vacancies_count




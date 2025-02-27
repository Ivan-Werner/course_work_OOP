import unittest
import pytest
from unittest.mock import MagicMock, patch, Mock
from src.api import APIHeadHunter

@pytest.fixture()
def api_client():
    return APIHeadHunter()

@pytest.fixture(scope='session')
def success_hh_response_body():
    return {'items': [{'id': 1}]}


@patch('requests.get')
def test_get_vacancies_success(mocked_get, api_client, success_hh_response_body):
    mocked_response = Mock(status_code=200)
    mocked_response.json.return_value = success_hh_response_body
    mocked_get.return_value = mocked_response

    response = api_client.get_vacancies('python')

    assert response == success_hh_response_body['items']


@patch('requests.get')
def test_get_vacancies_error(mocked_get, api_client, success_hh_response_body):
    mocked_response = Mock(status_code=400)
    mocked_response.json.return_value = {'error': 'Something go wrong'}
    mocked_get.return_value = mocked_response

    response = api_client.get_vacancies('python')

    assert response == []
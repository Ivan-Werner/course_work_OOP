import os
import pytest

from src.api import APIHeadHunter
from src.vacancy import Vacancy

@pytest.fixture
def vacancy():
    return Vacancy("Помощник фотографа",
                   "Алматы",
                   "Умение работать с детьми, вежливость, аккуратность, пунктуальность.",
                   100000,
                   0,
                   "https://hh.ru/vacancy/117261098"
                   )


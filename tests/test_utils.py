from src.utils import top_vacancy, filter_city



test_list =[
{
        "name": "Менеджер в отдел продаж",
        "city": "Алматы",
        "requirements": "У тебя грамотная речь. Ты хочешь хорошо зарабатывать. Ты открыт к новым знаниям. У тебя нет отвлекающих от работы факторов. ",
        "salary_from": 300000,
        "salary_to": 600000,
        "url": "https://hh.ru/vacancy/116800921"
    },
    {
        "name": "Помощник фотографа",
        "city": "Алматы",
        "requirements": "Умение работать с детьми, вежливость, аккуратность, пунктуальность.",
        "salary_from": 100000,
        "salary_to": 0,
        "url": "https://hh.ru/vacancy/117261098"
    },
    {
        "name": "Няня",
        "city": "Москва",
        "requirements": "Желателен педагогический/медицинский университет или курсы. Знание систем развития (монтессори, 7 гномов и др.). Опыт работы с детьми в возрасте...",
        "salary_from": 90000,
        "salary_to": 150000,
        "url": "https://hh.ru/vacancy/117527024"
    }
]

def test_top_vacancy():
    assert top_vacancy(number= "", vacancies_list=[1, 2, 3]) == [1, 2, 3]
    assert top_vacancy(number=2, vacancies_list=[1, 2, 3]) == [1, 2]

def test_filter_city_empty():
    assert filter_city(main_vacancies_list=[]) == []



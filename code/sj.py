import requests
from pprint import pprint

from common import format_statistics, predict_rub_salary


def get_sj_statistics(language, token):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    vacancy_page = 0
    vacancy_pages = 1
    vacancies_processed  = 0
    all_salary  = 0
    specialization = 48
    headers = {
        "X-Api-App-Id": token
    }
    while vacancy_page < vacancy_pages:
        count = 100
        moscow_id = 4
        params = {
            "keyword": language,
            "town": moscow_id,
            "count": count,
            "page": vacancy_page,
            "catalogues": specialization,
            "currency": "rub"
        }
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        vacancies = response.json()
        for vacancy in vacancies['objects']:
            predicted_salary = predict_rub_salary(vacancy['payment_from'], vacancy['payment_to'])
            if predicted_salary:
                vacancies_processed +=1
                all_salary += predicted_salary
        vacancy_page+=1
        vacancy_pages = vacancies['total']/count

    return all_salary, vacancies_processed, vacancies['total']



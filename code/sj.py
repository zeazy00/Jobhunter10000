import os
import requests
from dotenv import load_dotenv
from pprint import pprint

from common import get_language_statistics


def get_sj_vacancies(language):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    vacancy_page = 0
    vacancy_pages = 1
    vacancies_processed  = 0
    all_salary  = 0
    load_dotenv()
    headers = {
        "X-Api-App-Id": os.getenv("TOKEN")
    }
    while vacancy_page < vacancy_pages:
        count = 100
        params = {
            "keyword": language,
            "town": "4",
            "count": count,
            "page": vacancy_page,
            "catalogues": 48,
            "currency": "rub"
        }
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        vacancies = response.json()
        for vacancy in vacancies['objects']:
            predicted_salary = predict_rub_salary(vacancy)
            if predicted_salary:
                vacancies_processed +=1
                all_salary += predicted_salary
        vacancy_page+=1
        vacancy_pages = vacancies['total']/count

    return get_language_statistics(all_salary, vacancies_processed, vacancies['total'])


def predict_rub_salary(vacancy):
    if vacancy.get('payment_from') and vacancy.get('payment_to'):
        return((vacancy.get('payment_from')+vacancy.get('payment_to'))/2)
    elif vacancy.get('payment_from'):
        return(vacancy.get('payment_from')*1.2)
    elif vacancy.get('payment_to'):
        return(vacancy.get('payment_to')*0.8)

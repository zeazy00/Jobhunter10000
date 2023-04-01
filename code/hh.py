import requests

from common import get_language_statistics


def get_hh_vacancies(language):
    url = 'https://api.hh.ru/vacancies'
    vacancy_page = 0
    vacancy_pages = 1
    vacancies_processed  = 0
    all_salary  = 0
    while vacancy_page < vacancy_pages:
        params = {
        "text": f"Программист {language}",
        "area": 1,
        "period": 30,
        "per_page": 100,
        "page": vacancy_page
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        vacancies = response.json()
        for vacancy in vacancies["items"]:
            predicted_salary = predict_rub_salary(vacancy)
            if predicted_salary:
                vacancies_processed +=1
                all_salary += predicted_salary
        vacancy_page+=1
        vacancy_pages = vacancies["pages"]

    return get_language_statistics(all_salary ,vacancies_processed, vacancies["found"])


def predict_rub_salary(vacancy):
    if vacancy['salary'] and vacancy['salary']['currency'] == 'RUR':
        if vacancy['salary']['from'] and vacancy['salary']['to']:
            return((vacancy['salary']['from']+vacancy['salary']['to'])/2)
        elif vacancy['salary']['from']:
            return(vacancy['salary']['from']*1.2)
        elif vacancy['salary']['to']:
            return(vacancy['salary']['to']*0.8)
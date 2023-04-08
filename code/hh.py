import requests

from common import format_statistics, predict_rub_salary


def get_hh_statistics(language):
    url = 'https://api.hh.ru/vacancies'
    vacancy_page = 0
    vacancy_pages = 1
    vacancies_processed  = 0
    all_salary  = 0
    moscow_id = 1
    period_in_days = 30
    per_page = 100
    while vacancy_page < vacancy_pages:
        params = {
        "text": f"Программист {language}",
        "area": moscow_id,
        "period": period_in_days,
        "per_page": per_page,
        "page": vacancy_page
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        vacancies = response.json()
        for vacancy in vacancies["items"]:
            if vacancy['salary'] and vacancy['salary']['currency'] == 'RUR':
                predicted_salary = predict_rub_salary(vacancy['salary']['from'], vacancy['salary']['to'])
            else:
                predicted_salary = None
            if predicted_salary:
                vacancies_processed += 1
                all_salary += predicted_salary
        vacancy_page += 1
        vacancy_pages = vacancies["pages"]

    return all_salary, vacancies_processed, vacancies["found"]

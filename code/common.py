
def get_language_statistics(all_salary, vacancies_processed, vacancies_found):
    try:
        average_salary = int(all_salary/vacancies_processed)
    except ZeroDivisionError:
        average_salary = None
        
    language_vacancies_info = { 
        "vacancies_found": vacancies_found,
        "vacancies_processed": vacancies_processed,
        "average_salary": average_salary
    }
    return language_vacancies_info


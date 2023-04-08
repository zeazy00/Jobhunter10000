def format_statistics(all_salary, vacancies_processed, vacancies_found):
    try:
        average_salary = int(all_salary/vacancies_processed)
    except ZeroDivisionError:
        average_salary = None
        
    vacancies_statistics = { 
        "vacancies_found": vacancies_found,
        "vacancies_processed": vacancies_processed,
        "average_salary": average_salary
    }
    return vacancies_statistics


def predict_rub_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return (salary_from+salary_to)/2
    elif salary_from:
        return (salary_from*1.2)
    elif salary_to:
        return (salary_to*0.8)
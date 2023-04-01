from pprint import pprint
from os import system
from terminaltables import SingleTable

from hh import get_hh_vacancies
from sj import get_sj_vacancies


def main():
	languages = [
		"Python",
		"C",
		"Java",
		"C++",
		"C#",
		"Visual Basic",
		"JavaScript",
		"SQL",
		"Assembly language",
		"Swift"
	]
	hh_table_info = [["language", "vacancies found", "vacancies processed", "average salary"]]
	sj_table_info = [["language", "vacancies found", "vacancies processed", "average salary"]]

	for language in languages:
		hh_info = get_hh_vacancies(language)
		line_table_info = [language, hh_info["vacancies_found"], hh_info["vacancies_processed"], hh_info["average_salary"]]
		hh_table_info.append(line_table_info)

		sj_info = get_sj_vacancies(language)
		line_table_info = [language, sj_info["vacancies_found"], sj_info["vacancies_processed"], sj_info["average_salary"]]
		sj_table_info.append(line_table_info)

		system("cls")
		table_instance = SingleTable(hh_table_info, "HeahHunter vacancies")
		print(table_instance.table)
		print()
		table_instance = SingleTable(sj_table_info, "SuperJob vacancies")
		print(table_instance.table)


if __name__ == '__main__':
	main()
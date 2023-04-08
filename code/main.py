from dotenv import load_dotenv
from pprint import pprint
from os import getenv, system 
from terminaltables import SingleTable

from common import format_statistics
from hh import get_hh_statistics
from sj import get_sj_statistics


def main():
	load_dotenv()
	token = getenv("SUPERJOB_TOKEN")
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
	hh_table_statistics = [["language", "vacancies found", "vacancies processed", "average salary"]]
	sj_table_statistics = [["language", "vacancies found", "vacancies processed", "average salary"]]

	for language in languages:
		hh_statistics = get_hh_statistics(language)
		formated_statistics =  format_statistics(*hh_statistics)
		line_table = [language, formated_statistics["vacancies_found"], formated_statistics["vacancies_processed"], formated_statistics["average_salary"]]
		hh_table_statistics.append(line_table)

		sj_statistics = get_sj_statistics(language, token)
		formated_statistics =  format_statistics(*sj_statistics)
		line_table = [language, formated_statistics["vacancies_found"], formated_statistics["vacancies_processed"], formated_statistics["average_salary"]]
		sj_table_statistics.append(line_table)

		system("cls")
		table_instance = SingleTable(hh_table_statistics, "HeahHunter vacancies")
		print(table_instance.table)
		print()
		table_instance = SingleTable(sj_table_statistics, "SuperJob vacancies")
		print(table_instance.table)


if __name__ == '__main__':
	main()
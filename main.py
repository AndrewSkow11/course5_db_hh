from tabulate import tabulate
from src.db_manager import DBManager
from src.hh_api_manager import HhAPIManager


# подготовка к работе (создание базы данных и таблиц)
db_manager = DBManager()
# db_manager.create_database()
# db_manager.create_tables()

# Создание списка работодателей
# list_of_employers = HhAPIManager.get_list_employers()
# print(list_of_employers)

# hh = HhAPIManager.add_to_table()

task = input(
            "Введите 1, чтобы получить список всех компаний и количество вакансий у каждой компании\n"
            "Введите 2, чтобы получить список всех вакансий с указанием названия компании, "
            "названия вакансии и зарплаты и ссылки на вакансию\n"
            "Введите 3, чтобы получить среднюю зарплату по вакансиям\n"
            "Введите 4, чтобы получить список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
            "Введите 5, чтобы получить список всех вакансий, в названии которых содержатся переданные в метод слова\n"
            "Введите Стоп, чтобы завершить работу\n"
            ">> "
        )

if task == "Стоп":
    exit()

elif task == '1':
    print(tabulate(db_manager.get_companies_and_vacancies_count()))

elif task == '2':
    print(tabulate(db_manager.get_all_vacancies()))

elif task == '3':
    print( tabulate( db_manager.get_avg_salary()))

elif task == '4':
    print(tabulate(db_manager.get_vacancies_with_higher_salary()))

elif task == '5':
    keyword = input('Введите ключевое слово: ')
    print(tabulate(db_manager.get_vacancies_with_keyword(keyword)))

else:
    print('Неправильный запрос')












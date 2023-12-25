from src.db_manager import DBManager
from src.hh_api_manager import HhAPIManager

# подготовка к работе (создание базы данных и таблиц)
db_manager = DBManager()
db_manager.create_database()
db_manager.create_tables()

# Создание списка работодателей
list_of_employers = HhAPIManager.get_list_employers()
print(list_of_employers)

# hh = HhAPIManager.add_to_table()
#
# input("Для получения список всех компаний и количество вакансий у каждой компании нажмите ENTER\n")
# db_manager.get_companies_and_vacancies_count()




from src.db_manager import DBManager
from src.hh_api_manager import HhAPIManager

# подготовка к работе (создание базы данных и таблиц)
db_manager = DBManager()
db_manager.create_database()
db_manager.create_tables()

# Создание списка работодателей
list_of_employers = HhAPIManager.get_list_employers()



# print(list_of_employers)



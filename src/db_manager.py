# Создать класс DBManager для работы с данными в БД.
#
# Класс DBManager
# Создайте класс DBManager,
# который будет подключаться к БД PostgreSQL и иметь следующие методы:
#
# get_companies_and_vacancies_count()
#  — получает список всех компаний и количество вакансий у каждой компании.
#
# get_all_vacancies()
#  — получает список всех вакансий с указанием названия компании,
# названия вакансии и зарплаты и ссылки на вакансию.
#
# get_avg_salary()
#  — получает среднюю зарплату по вакансиям.
#
# get_vacancies_with_higher_salary()
#  — получает список всех вакансий, у которых зарплата выше средней
# по всем вакансиям.
#
# get_vacancies_with_keyword()
#  — получает список всех вакансий, в названии которых содержатся переданные
# в метод слова, например python.
#
# Класс DBManager должен использовать библиотеку psycopg2 для работы с БД.

import psycopg2


class DBManager:

    def __init__(self, host='localhost', database='hh_vacancies',
                 user='postgres', password='99-100'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def create_database(self):
        """Создание базы данных и таблиц"""

        conn = psycopg2.connect(host=self.host, database='postgres',
                                user=self.user, password=self.password)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute("DROP DATABASE IF EXISTS hh_vacancies")
        cur.execute("CREATE DATABASE hh_vacancies")

        conn.close()

        print("\nБаза данных создана и подготовлена к работе ...")

    def create_tables(self):
        conn = psycopg2.connect(host=self.host, database=self.database,
                                user=self.user, password=self.password)
        with conn.cursor() as cur:
            cur.execute("""
                        CREATE TABLE employers (
                        employer_id INTEGER PRIMARY KEY,
                        company_name varchar(255),
                        open_vacancies INTEGER
                        )""")

            cur.execute("""
                        CREATE TABLE vacancies (
                        vacancy_id SERIAL PRIMARY KEY,
                        vacancies_name varchar(255),
                        payment INTEGER,
                        requirement TEXT,
                        vacancies_url TEXT,
                        employer_id INTEGER REFERENCES employers(employer_id)
                        )""")

        conn.commit()
        conn.close()
        print("Таблицы в базе данных созданы успешно ...")



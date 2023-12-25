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

    def get_companies_and_vacancies_count(self):
        """Метод получает список всех компаний и количество вакансий
         у каждой компании"""

        with psycopg2.connect(host=self.host, database=self.database,
                              user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT company_name, COUNT(vacancies_name)"
                            f" AS count_vacancies  "
                            f"FROM employers "
                            f"JOIN vacancies USING (employer_id) "
                            f"GROUP BY employers.company_name")
                result = cur.fetchall()
            conn.commit()
        return result

    def get_all_vacancies(self):
        """Метод получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию"""
        with psycopg2.connect(host=self.host, database=self.database,
                              user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT employers.company_name,"
                            f" vacancies.vacancies_name, "
                            f"vacancies.payment, vacancies_url "
                            f"FROM employers "
                            f"JOIN vacancies USING (employer_id)")
                result = cur.fetchall()
            conn.commit()
        return result

    def get_avg_salary(self):
        """Метод получает среднюю зарплату по вакансиям"""
        with psycopg2.connect(host=self.host, database=self.database,
                              user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT AVG(payment) as avg_payment"
                            f" FROM vacancies ")
                result = cur.fetchall()
            conn.commit()
        return result

    def get_vacancies_with_higher_salary(self):
        """Метод получает список всех вакансий,
        у которых зарплата выше средней по всем вакансиям"""
        with psycopg2.connect(host=self.host, database=self.database,
                              user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM vacancies "
                            f"WHERE payment > (SELECT AVG(payment)"
                            f" FROM vacancies) ")
                result = cur.fetchall()
            conn.commit()
        return result

    def get_vacancies_with_keyword(self, keyword):
        """Метод получает список всех вакансий,
        в названии которых содержатся переданные в метод слова"""
        with psycopg2.connect(host=self.host, database=self.database,
                              user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM vacancies "
                            f"WHERE lower(vacancies_name) LIKE '%{keyword}%'")
                result = cur.fetchall()
            conn.commit()
            if len(result) == 0:
                print("Вакансий не найдено ...")
        return result

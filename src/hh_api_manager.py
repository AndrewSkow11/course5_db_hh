import requests
import psycopg2


class HhAPIManager:
    """Класс позволяет получать данные с hh.ru"""

    @staticmethod
    def get_list_employers():
        """Метод позволяет получать список работодателей"""

        list_of_employers = []

        params_for_russia = {
            'area': 113,
            'page': 0,
            'per_page': 100
        }

        params_for_ukraine = {
            'area': 5,
            'page': 0,
            'per_page': 100
        }

        params_for_belarus = {
            'area': 16,
            'page': 0,
            'per_page': 100
        }

        url = "https://api.hh.ru/employers/"
        data_employers_ru = requests.get(url, params=params_for_russia).json()
        data_employers_uk = requests.get(url, params=params_for_ukraine).json()
        data_employers_rb = requests.get(url, params=params_for_belarus).json()

        for employer in data_employers_ru['items']:
            if employer['open_vacancies'] > 0:
                list_of_employers.append(employer['id'])

        for employer in data_employers_uk['items']:
            if employer['open_vacancies'] > 0:
                list_of_employers.append(employer['id'])

        for employer in data_employers_rb['items']:
            if employer['open_vacancies'] > 0:
                list_of_employers.append(employer['id'])

        print("Список компаний-работодателей сформирован ... "
              "Ожидайте обработки данных ...")
        return list_of_employers

    def get_employer(employer_id):
        """Получение данных о работодателей по API"""

        url = f"https://api.hh.ru/employers/{employer_id}"
        data_vacancies = requests.get(url).json()

        employer = {
            "employer_id": int(employer_id),
            "company_name": data_vacancies['name'],
            "open_vacancies": data_vacancies['open_vacancies']
        }
        return employer

    def get_vacancies(employer_id):
        """Получение данных вакансий по API"""
        params = {
            'page': 0,
            'per_page': 100,
        }
        url = f"https://api.hh.ru/vacancies?employer_id={employer_id}"
        data_vacancies = requests.get(url, params=params).json()

        vacancies_list = []

        for item in data_vacancies["items"]:
            vacancy = {
                'vacancy_id': int(item['id']),
                'vacancies_name': item['name'],
                'payment': item["salary"]["from"] if item["salary"] else None,
                'requirement': item['snippet']['requirement'],
                'vacancies_url': item['alternate_url'],
                'employer_id': employer_id
            }

            if vacancy['payment'] is not None:
                vacancies_list.append(vacancy)

            return vacancies_list

    @staticmethod
    def add_to_table():
        """Заполнение таблиц по списку работодателей"""

        employers_list = HhAPIManager.get_list_employers()

        with psycopg2.connect(host="localhost", database="hh_vacancies",
                              user="postgres", password="99-100") as conn:
            with conn.cursor() as cur:
                cur.execute('TRUNCATE TABLE employers, vacancies '
                            'RESTART IDENTITY;')

                for employer in employers_list:
                    employer_list = HhAPIManager.get_employer(employer)
                    cur.execute('INSERT INTO employers (employer_id,'
                                ' company_name, open_vacancies) '
                                'VALUES (%s, %s, %s) RETURNING employer_id',
                                (employer_list['employer_id'],
                                 employer_list['company_name'],
                                 employer_list['open_vacancies']))

                for employer in employers_list:
                    vacancy_list = HhAPIManager.get_vacancies(employer)
                    for v in vacancy_list:
                        cur.execute('INSERT INTO vacancies (vacancy_id,'
                                    ' vacancies_name, '
                                    'payment, requirement, vacancies_url, '
                                    'employer_id) '
                                    'VALUES (%s, %s, %s, %s, %s, %s)',
                                    (v['vacancy_id'], v['vacancies_name'],
                                     v['payment'],
                                     v['requirement'], v['vacancies_url'],
                                     v['employer_id']))

            conn.commit()

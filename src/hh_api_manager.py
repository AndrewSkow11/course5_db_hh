import requests


class HhAPIManager:
    """Класс позволяет получать данные с hh.ru"""

    @staticmethod
    def get_list_employers(numbers=10):
        """Метод позволяет получать список работодателей"""

        list_of_employers = []

        url = "https://api.hh.ru/employers/"
        data_employers = requests.get(url).json()

        for num in range(numbers):
            list_of_employers.append(data_employers['items'][num]['id'])

        # print(data_employers['items'][0]['id'])
        # print(data_employers['items'][1]['id'])



        hh_employers = {
            # "employer_id": int(employer_id),
            # "company_name": data_vacancies['name'],
            # "open_vacancies": data_vacancies['open_vacancies']
        }

        print(list_of_employers)
        return list_of_employers


# hh_api = HhAPIManager()
# hh_api.get_list_employers()

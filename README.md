# Курсовой проект №5 

## Описание проекта 

Приложение позволяет находить и фильтровать вакансии по работодателям с платформы hh.ru. 

Используется хранение результатов поиска в базе данных. Запросы осуществляются в сохранённой базе данных. 

Поиск работодателей осуществляется по следующим параметрам:
* наличие открытых вакансий;
* территория России, Украины, Беларуси. 

## Стек технологий: 
* Python3
* PostgreSQL

## Библиотеки Python3:
* tabulate (для форматированного вывода запросов из базы данных);
* colorama (для выделения цветом консольного вывода);
* psycopg2 (для работы с базой данных);
* requests (для запросов к платформе hh.ru)

## Развёртывание проекта (требования):
* установка библиотек (можно использовать: pip install tabulate, pip install colorama и т.д.);
* установленный PostgreSQL (должна быть база "postgres" для первичного подключения);
* во время работы программы не должно быть обращения к базе другими пользователями или процессами, иначе возникнет ошибка;
* личные параметры вашей базы необходимо задать в методе \_\_init__() класса DBManager (строки 6-7), а также в методе add_to_table() класса HhAPIManager (строки 98-99).

## Автор проекта: 
Андрей Сковородников (https://github.com/AndrewSkow11)


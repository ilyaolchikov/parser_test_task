# Задача

Даны два файла со списком работ: excel и json. Необходимо разработать консольное приложение на python, которое будет
считывать этот файл с жесткого диска, парсить и сохранять информацию в таблицу БД.
Вызов приложения из командной строки, пример:
> python main.py loader C:\data\works.xlsx

или

> python main.py loader C:\data\works.json

База данных может быть любая, например, PostgreSQL.

ID:int – для этого поля установить автоинкремент
WBS: char(512) – для этого поля необходимо создать уникальный индекс
EFFORT:float – для этого поля задать значение по умолчанию равное 0
NAME:char(512)
START_DATE:date
END_DATE:date

# Комментарии к решению:

1. Реализована возможность расширять приложение, добавив новую СУБД за счет имплементации класса BaseDatabase.
2. Используется паттерн Singleton для создания экземпляра класса СУБД.
3. Создан класс ParserFactory и его наследники для создания парсеров, возможно, это лишнее на данный момент, тк логика
   создания парсеров простая, но такое решение является полезным инструментом при расширении функционала.
4. Можно было бы добавить отдельный класс Logger для более корректной обработки исключений + отображения ошибок в разных
   режимах (файл, консоль и тд).
5. Сейчас класс PostgreSqlDatabase не очень аккуратно работает с таблицей "works", но я думаю, этого достаточно для
   тестового задания. Можно было бы реализовать собственный класс для работы с таблицей, чтобы избежать проблем в
   будущем.


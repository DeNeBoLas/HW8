from datetime import datetime, timedelta
import collections
import calendar
import sys

test_users = [
    {"name": "Kate", "birthday": datetime(year=2012, month=8, day=2)},  # "02.08.2012"
    {"name": "Alex", "birthday": datetime(year=2005, month=8, day=5)},  # "05.08.2005"
    {"name": "Sem", "birthday": datetime(year=2002, month=8, day=12)},  # "12.08.2002"
    {
        "name": "Nataly",
        "birthday": datetime(year=2000, month=8, day=15),
    },  # "15.08.2000"
    {
        "name": "Nic",
        "birthday": datetime(year=2015, month=8, day=8),
    },  # "10.08.2015" Monday
    {"name": "Max", "birthday": datetime(year=2001, month=7, day=31)},  # "31.07.2001"
    {"name": "Leo", "birthday": datetime(year=2005, month=8, day=1)},  # "01.08.2005"
    {"name": "Bill", "birthday": datetime(year=2003, month=8, day=3)},  # "01.08.2005"
    {"name": "Kim", "birthday": datetime(year=2000, month=8, day=2)},  # "01.08.2005"
]

"""Завдання

Вам потрібно реалізувати корисну функцію для виведення списку колег, яких потрібно привітати з днем народження на тижні.

У вас є список словників users, кожен словник у ньому обов'язково має ключі name та birthday. Така структура представляє модель списку користувачів з їх іменами та днями народження. name — це рядок з ім'ям користувача, а birthday — це datetime об'єкт, в якому записаний день народження.

Ваше завдання написати функцію get_birthdays_per_week, яка отримує на вхід список users і виводить у консоль (за допомогою print) список користувачів, яких потрібно привітати по днях.
Умови приймання
get_birthdays_per_week виводить іменинників у форматі:

Monday: Bill, Jill
Friday: Kim, Jan

Користувачів, у яких день народження був на вихідних, потрібно привітати в понеділок.
Для тестування зручно створити тестовий список users та заповнити його самостійно.
Функція виводить користувачів з днями народження на тиждень вперед від поточного дня.
Тиждень починається з понеділка."""

res = []  # data for values(names)

days_dict = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": [],
}  # data for keys


def get_birthdays_per_week(users: list) -> dict:
    for user in users:
        day_of_birthday = user["birthday"].strftime("%A")

        if day_of_birthday == "Monday":
            days_dict["Monday"].append(user["name"])
        elif day_of_birthday == "Tuesday":
            days_dict["Tuesday"].append(user["name"])
        elif day_of_birthday == "Wednesday":
            days_dict["Wednesday"].append(user["name"])
        elif day_of_birthday == "Thursday":
            days_dict["Thursday"].append(user["name"])
        elif day_of_birthday == "Friday":
            days_dict["Friday"].append(user["name"])
        elif day_of_birthday == "Saturday":
            days_dict["Saturday"].append(user["name"])
        elif day_of_birthday == "Sunday":
            days_dict["Sunday"].append(user["name"])
    # print(days_dict)

    today = datetime.now().strftime("%A")


# if __name__ == '__main__':
# sys.stdout =

a = get_birthdays_per_week(test_users)

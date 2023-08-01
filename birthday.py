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

from datetime import datetime, timedelta
import collections
import calendar


test_users = [
    {"name": "Kate", "birthday": datetime(year=2012, month=8, day=2)},  # "02.08.2012"
    {"name": "Alex", "birthday": datetime(year=2005, month=8, day=4)},  # "05.08.2005"
    {"name": "Sem", "birthday": datetime(year=2002, month=8, day=7)},  # "12.08.2002"
    {
        "name": "Nataly",
        "birthday": datetime(year=2000, month=8, day=6),
    },  # "15.08.2000"
    {
        "name": "Nic",
        "birthday": datetime(year=2015, month=8, day=8),
    },  # "10.08.2015" Monday
    {"name": "Max", "birthday": datetime(year=2001, month=8, day=5)},  # "31.07.2001"
    {"name": "Leo", "birthday": datetime(year=2005, month=8, day=1)},  # "01.08.2005"
    {"name": "Bill", "birthday": datetime(year=2003, month=8, day=3)},  # "03.08.2005"
    {"name": "Kim", "birthday": datetime(year=2000, month=8, day=2)},  # "01.08.2005"
]
days_dict = {}  # data for keys
for i in range(7):
    days_dict[i] = []


def get_birthdays_per_week(users: list) -> dict:
    today = datetime.now()
    next_week = today + timedelta(weeks=1)

    for user in users:
        birthdays_in_this_year = user["birthday"].replace(year=today.year)

        if today <= birthdays_in_this_year < next_week:
            day_of_week = birthdays_in_this_year.weekday()

            if (
                birthdays_in_this_year.weekday() == 5
                or birthdays_in_this_year.weekday() == 6
            ):
                days_dict[0].append(user["name"])
            else:
                days_dict[day_of_week].append(user["name"])

    out_days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    for k, v in days_dict.items():
        if len(v) == 0:
            continue
        day = out_days[k]
        print(f"{day}: {','.join(v)}")


if __name__ == "__main__":
    get_birthdays_per_week(test_users)

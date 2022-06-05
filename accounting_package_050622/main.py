import datetime as dt
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    calc_sal = calculate_salary()
    get_empl = get_employees()
    print(f'Today is: {dt.date.today()}. \nThe result of first method is: {calc_sal} \nThe result of the second method'
          f' is: {get_empl}')

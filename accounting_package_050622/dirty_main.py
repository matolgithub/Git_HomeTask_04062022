from accounting_package_050622.application.salary import *
from accounting_package_050622.application.db.people import *

if __name__ == "__main__":
   print(f'{calculate_salary()}\n{get_employees()}')
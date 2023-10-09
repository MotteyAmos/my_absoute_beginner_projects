import json

def great_user():
    try:
        with open('json_file3.json') as f:
            user_name = json.load(f)
            print(user_name + " you are welcome")
    except FileNotFoundError as f:
        user_name = input("Enter your user name: ")
        with open("json_file23.json", 'w') as f:
            json.dump(user_name, f)
            print(user_name + " you are welcome")


great_user()


def add(x, y):
    # add function
    return x + y


def subtract(x, y):
    # subtract function
    return x - y


def multiple(x, y):
    # multiplication function
    return x * y


def divide(x, y):
    # division function
    return x / y


class Employee:
    def __init__(self, first_name, last_name, anual_salary, bonus_salary=''):
        self.first_name = first_name
        self.last_name = last_name
        self.anual_salary = anual_salary
        self.bonus_salary = bonus_salary

    def default_raise(self):
        return self.anual_salary + 5000

    def custom_raise(self):
        if self.bonus_salary:
            salary = self.default_raise() + self.bonus_salary
        else:
            salary = self.default_raise()
        return "{} {} salary current salary is {}".format(self.last_name, self.first_name, salary)

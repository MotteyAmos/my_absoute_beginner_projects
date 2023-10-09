import csv


class Item:
    pay_rate = 0.5
    instances = []

    def __init__(self, name=str(), price=float(), quantity=float()):
        # check validation to the received arguments
        while True:
            try:
                try:
                    assert price >= 0, f"please enter price greate than 0 that is it should be positive"

                except:
                    print("please your price should be greater than zero not negetive numebers not allowed")
                    price = float(input("Enter the price again: "))

                try:
                    assert quantity >= 0
                except:
                    print("please your quantity should be greater than zero not negetive numebers not allowed")
                    quantity = float(input("please type the quantity again: "))
            except ValueError:
                continue
            if quantity >= 0 and price >= 0:
                break

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity
        Item.instances.append(self)

    @classmethod
    def intantiate_from_csv(cls):
        with open("index.csv", "r") as f:
            reader = csv.DictReader(f)
            reader = list(reader)

        for item in reader:
            Item(
                item.get('name'),
                float(item.get('price')),
                int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # check if the value entered is an integer or not
        if isinstance(num, float):
            # return true if the value enter is an float with 0 decimal places
            # i.e 5.0 3.0
            return num.is_integer()
        elif isinstance(num, int):
            # return true if it is an integer
            # i.e 5, 2, 10
            return True
        else:
            return False

    @property
    def name(self):
        return self.__name + " uou ve"
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("This name is too long")
        else:
            self.__name = value
    @name.deleter
    def name(self):
        msg = input("Are you sure you want to delete name (y/n): ")
        if msg.lower() == "y":
            self.name = ''
        else:
            self.name = self.name
    @property
    def price(self):
        return "the price is " + str(self.__price)

    def __repr__(self):
        return f"{self.__class__.__name__}, {self.name}, {self.__price}, {self.quantity}"

    def calculate_total_price(self, increment_value):
        return self.__price * self.quantity + increment_value

    def discount(self):
        return self.calculate_total_price() * self.pay_rate

    def __connect(self):
        pass
    def __email_msg(self):
        return f"""
        I was trying to send something to you through an email
                """
    def __send(self):
        pass
    def email(self):
        self.__connect()
        print(self.__email_msg())
        self.__send()

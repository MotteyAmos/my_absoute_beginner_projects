import csv
from class_learn1 import Item


class Phone(Item):
    def __init__(self, num_of_broken_items = int(), name= str(), price= float(), quantity= float() ):
        super().__init__(name, price, quantity)
        self.num_of_broken_item = num_of_broken_items



import string


class Product():

    def __init__(self, name, amount) -> None:
        self.name = name
        self.amount = amount
        self.data = f"Product: {self.name} \nAvailables: {self.amount}\n"


    def show_data(self) -> str :
        return self.data
from Product import *
import Constants

class TV(Product):

    def __init__(self) -> None:
        self.name = 'TV'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)

class Blender(Product):

    def __init__(self) -> None:
        self.name = 'Blender'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)

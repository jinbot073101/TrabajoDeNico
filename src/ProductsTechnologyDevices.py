from Product import *
import Constants

class LaptopNoOS(Product):

    def __init__(self) -> None:
        self.name = 'Laptop without Operating system'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)


class MacLatop(Product):

    def __init__(self) -> None:
        self.name = 'Mac laptop'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)


class Tablet(Product):

    def __init__(self) -> None:
        self.name = 'Tablet'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)


class Smartwatch(Product):

    def __init__(self) -> None:
        self.name = 'Smartwatch'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)




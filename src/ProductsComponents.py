from Product import *
import Constants

class Microcontroller(Product):

    def __init__(self) -> None:
        self.name = 'Microcontroller'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)


class Pickit(Product):

    def __init__(self) -> None:
        self.name = 'Pickit programmer'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)


class RasperryPi(Product):

    def __init__(self) -> None:
        self.name = 'Rasperry Pi'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)



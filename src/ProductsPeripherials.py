from Product import *
import Constants

class Keyboard(Product):

    def __init__(self) -> None:
        self.name = 'Keyboard'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)


class GraphicTablet(Product):

    def __init__(self) -> None:
        self.name = 'Graphical drawing tablet'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)


class MultipleCharger(Product):

    def __init__(self) -> None:
        self.name = 'Multiple charger'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)


class Baffle(Product):

    def __init__(self) -> None:
        self.name = 'Baffle'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)



from Product import *
import Constants

class Camera(Product):

    def __init__(self) -> None:
        self.name = 'Camera'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)


class CameraPro(Product):

    def __init__(self) -> None:
        self.name = 'Professional Camera'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)



from Category import *
from ProductsCamera import *
from ProductsComponents import *
from ProductsPeripherials import *
from ProductsTechnologyDevices import *
from ProductsTechnologyHome import *

class CategoryCamera(Category):

    def __init__(self) -> None:
        self.name = 'Camera'
        self.products_list = [Camera(),CameraPro()]
        super().__init__(self.name, self.products_list)


class CategoryComponents(Category):

    def __init__(self) -> None:
        self.name = 'Electronic components'
        self.products_list = [Microcontroller(),Pickit(), RasperryPi()]
        super().__init__(self.name, self.products_list)

class CategoryPeripherials(Category):

    def __init__(self) -> None:
        self.name = 'Peripherials devices'
        self.products_list = [Keyboard(),GraphicTablet(), MultipleCharger(), Baffle()]
        super().__init__(self.name, self.products_list)

class CategoryTecnologyDevices(Category):

    def __init__(self) -> None:
        self.name = 'Technology devices'
        self.products_list = [LaptopNoOS(),MacLatop(), Tablet(), Smartwatch()]
        super().__init__(self.name, self.products_list)

class CategoryTechnologyHome(Category):

    def __init__(self) -> None:
        self.name = 'Technology home devices'
        self.products_list = [TV(),Blender()]
        super().__init__(self.name, self.products_list)
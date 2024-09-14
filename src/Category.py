from abc import ABC, abstractmethod

from Product import *

class Category(ABC):

    def __init__(self, name, productlist) -> None:
        self.name = name
        self.products_list = productlist

    def show_products(self) -> Product:
        return self.products_list
    
    
    

    
    

    


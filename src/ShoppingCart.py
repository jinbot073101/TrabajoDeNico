import string
from datetime import datetime

from Product import *


class ShoppingCart:

    def __init__(self) -> None:
        self.name = 'Shopping Cart'
        self.products_list = []

    def show_products(self) -> list[Product]:
        return self.products_list
    
    def add_product(self, product: Product) -> None:
        self.products_list.append(product)

    def make_check_out(self, name: str, direction: str) -> str:
        checkout = f"Checkout:\nName: {name}\nDirection: {direction}\nDate: {datetime.now()}\nProducts:\n"
        for product in self.products_list:
            checkout += f"{product.name}: {product.amount}\n"
        return checkout

    def __str__(self) -> str:
        if not self.products_list:
            return "The shopping cart is empty."
        products_str = "\n".join([f"{product.name}: {product.amount}" for product in self.products_list])
        return f"Shopping Cart:\n{products_str}"

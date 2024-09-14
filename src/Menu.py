import sys

import Constants
from CategoriesProducts import *
from ShoppingCart import *


class Menu:
    def __init__(self) -> None:
        self.shopping_cart = ShoppingCart()

    def back(self, option: int) -> None:
        if option == 1:
            self.display("\n<<Thanks for visiting us!>>")
            sys.exit()

    def get_input(self, text: str = None) -> str:
          return input(text) if text else input()

    def display(self, text: str) -> None:
        print(text)

    def display_categories(self, categories: list[Category]) -> None:
        self.display(Constants.MENU_2)
        for index, category in enumerate(categories, start=2):
            self.display(f"{index}. {category.name}")

    def display_products(self, category: Category) -> None:
        self.display(f"Products in {category.name}:")
        for index, product in enumerate(category.show_products(), start=1):
            if product.amount > 0:
                self.display(f"{index}. {product.show_data()}")
            else:
                self.display(f"{index}. {product.name} (Out of Stock)")

    def display_menu(self) -> None:
        self.display(Constants.MENU_1)

    def display_shopping_cart(self) -> None:
        if not self.shopping_cart.products_list:
            self.display("Your shopping cart is empty.")
        else:
            self.display("Your shopping cart contains:")
            for product in self.shopping_cart.products_list:
                self.display(f"{product.name} - Quantity: {product.amount}")

    def get_client_data(self) -> None:
        name = self.get_input("Type your name: ")
        direction = self.get_input("Type your direction: ")
        self.display(self.shopping_cart.make_check_out(name, direction))

    def process_cycle(self) -> None:
        categories = [
            CategoryCamera(), 
            CategoryComponents(), 
            CategoryPeripherials(), 
            CategoryTecnologyDevices(), 
            CategoryTechnologyHome()
        ]
        self.display_menu()

        while True:
            try:
                option = int(self.get_input())  # Opción inicial para el menú principal
                self.back(option)
                if option == 2:  # Ver catálogo
                    self.display_categories(categories)
                    category_option = int(self.get_input("Select a category: "))
                    self.back(category_option)
                    # Asegurarse de que la opción de categoría es válida
                    if 2 <= category_option < len(categories) + 2:
                        category_selected = categories[category_option - 2]
                        self.display_products(category_selected)   
                        while True:
                            product_option = int(self.get_input("Select a product or check shopping cart (2 to check cart): "))
                            self.back(product_option)
                            
                            if product_option == 2:  # Opción para ver el carrito
                                self.display_shopping_cart()  # Mostrar carrito
                                
                                checkout_option = int(self.get_input("Proceed to checkout? (1 to Exit, 2 to Continue): "))
                                self.back(checkout_option)
                                
                                if checkout_option == 2:
                                    self.get_client_data()
                                    break
                                
                            elif 3 <= product_option <= len(category_selected.products_list) + 2:
                                selected_product = category_selected.products_list[product_option - 3]
                                
                                if selected_product.amount > 0:
                                    self.shopping_cart.add_product(selected_product)
                                    self.display(f"Added to shopping cart: {selected_product.name}")
                                    selected_product.amount -= 1
                                    self.display_products(category_selected)  # Mostrar productos actualizados
                                else:
                                    self.display(f"{selected_product.name} is out of stock.")
                            else:
                                self.display("Invalid option. Please select a valid product.")
                                
                    else:
                        self.display("Invalid category selection. Please try again.")
            except ValueError:
                self.display("Please enter a valid number.")
            except IndexError:
                self.display("Option out of range. Please select a valid category.")



                        

                            

               
                    
            




                    


                
                 





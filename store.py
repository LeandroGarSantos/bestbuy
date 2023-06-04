from typing import List
from products import Product, LimitedProduct, NonStockedProduct, SpecialProduct


class Store:

    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        self.products.remove(product)

    # Now, the get_total_quantity() method checks if the quantity of each
    # product is finite (that is, not unlimited) before adding it to the total
    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            if product.quantity != float('inf'): # at this line
                total_quantity += product.quantity
        return total_quantity

    def get_all_products(self) -> List[Product]:
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

# Added one handle the error about MAXIMUM Product
    def order(self, shopping_list: List[tuple]) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            if product in self.products:
                try:
                    total_price += product.buy(quantity)
                except Exception as e:
                    if isinstance(product, LimitedProduct):
                        max_quantity = product.maximum
                        error_message = f"Quantity exceeds the maximum allowed for this product. Maximum quantity: {max_quantity}"
                        print(error_message)
                    else:
                        print(str(e))
        return total_price



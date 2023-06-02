class Product:

    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.price = price
        self.name = name
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity):
        if quantity <= 0:
            self.quantity = 0
            self.desactive()
        else:
            self.quantity = quantity

    def is_active(self) -> bool:
        return self.quantity > 0

    def activate(self):
        self.active = True

    def desactive(self):
        self.desactive = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        if not self.active:
            raise Exception("Product is not active")
        if quantity > self.quantity:
            raise Exception ("Insufficient quantity!")

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.desactive()
        return total_price


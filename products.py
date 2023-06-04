class Promotion:
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        pass


# Promo > Second Half price!
class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        promo_count = quantity // 2
        remaining_count = quantity % 2
        total_price = (product.price * promo_count) + (product.price * 0.5)
        return total_price


# Promo > Third One Free
class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        promo_count = quantity // 3
        remaining_count = quantity % 3
        total_count = promo_count * 2 + remaining_count
        total_price = product.price * total_count
        return total_price


# Promo > 30% off!
class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount_amount = product.price * self.percent / 100
        total_price = product.price * quantity - discount_amount
        return total_price


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
        self.promotion = None

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
        promotion_str = f", Promotion: \033[91m{self.promotion.name}\033[0m" if self.promotion else ", Promotion: \033[91mNone\033[0m"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_str}"

    def set_promotion(self, promotion):
        self.promotion = promotion

    def buy(self, quantity) -> float:
        if not self.active:
            raise Exception("Product is not active")
        if quantity > self.quantity:
            raise Exception("Insufficient quantity!")

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.desactive()
        return total_price


class SpecialProduct(Product):
    def __init__(self, name, price, quantity, special_feature):
        super().__init__(name, price, quantity)
        self.special_feature = special_feature

    def show(self) -> str:
        return f"{super().show()}, Special Feature: {self.special_feature}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, limited_offer, maximum):
        super().__init__(name, price, quantity)
        self.limited_offer = limited_offer
        self.maximum = maximum

    def show(self) -> str:
        return f"{super().show()}, Limited Offer: {self.limited_offer}, Maximum: {self.maximum}"


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, float('inf'))

    def set_quantity(self, quantity):
        pass  # No need to update the quantity for non-stocked products

    def show(self):
        promotion_str = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: Unlimited{promotion_str}"
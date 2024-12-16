from enum import Enum


class PaymentStatus(Enum):
    F = "FAILED"
    P = "PENDING"
    C = "COMPLETE"


class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = PaymentStatus.P.value

    def add_items(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor:
    def pay_with_debit_card(self, order: Order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

    def pay_with_credit_card(self, order: Order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

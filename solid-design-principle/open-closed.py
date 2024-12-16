from abc import ABC, abstractmethod
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


class PaymentProcessor(ABC):

    @abstractmethod
    def payment(self, order, security_code):
        pass


class DebitCardPaymentProcessor(PaymentProcessor):
    def payment(self, order, security_code):
        print(PaymentStatus.P.value)
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        PaymentStatus.C.value


class CreditCardPaymentProcessor(PaymentProcessor):
    def payment(self, order, security_code):
        print(PaymentStatus.P.value)
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        print(f"{PaymentStatus.C.value}")


class PaypalPaymentProcessor(PaymentProcessor):
    def payment(self, order, security_code):
        print(PaymentStatus.P.value)
        print("Processing paypal payment type")
        print(f"Verifying security code: {security_code}")
        PaymentStatus.C.value

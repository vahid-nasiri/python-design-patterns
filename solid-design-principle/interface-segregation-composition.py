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


class SMSAuthorizer:

    def __init__(self) -> None:
        self.authorized = False

    def verify_code(self, code) -> None:
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitCardPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: SMSAuthorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def payment(self, order):
        if not self.authorizer.is_authorized():
            print("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        PaymentStatus.C.value


class CreditCardPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def payment(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        PaymentStatus.C.value


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address, authorizer: SMSAuthorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def payment(self, order):
        if not self.authorizer.is_authorized():
            print("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        PaymentStatus.C.value

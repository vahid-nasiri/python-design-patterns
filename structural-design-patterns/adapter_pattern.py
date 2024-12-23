from abc import ABC, abstractmethod

class Target(ABC):

	@abstractmethod
	def request(self) -> str:
		pass

class Adaptee:
	def specific_request(self) -> str:
		return "Adaptee's specific request"

class Adapter(Target):
	def __init__(self, adaptee: Adaptee):
		self._adaptee = adaptee

	def request(self) -> str:
		return f"Adapted: {self._adaptee.specific_request()}"

adaptee = Adaptee()
adapter = Adapter(adaptee)
print(adapter.request())
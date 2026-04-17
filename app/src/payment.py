from typing import Protocol

class PaymentProtocol(Protocol):
    def process(self, amount: float) -> None:
        ...
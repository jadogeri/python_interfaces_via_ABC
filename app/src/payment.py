from typing import Protocol

class Payment(Protocol):
    def process(self, amount: float) -> None:
        ...
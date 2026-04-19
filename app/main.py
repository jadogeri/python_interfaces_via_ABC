"""
Payment System - Entry Point
----------------------------
Description: Orchestrates the execution of different payment methods
             using the Payment protocol.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2023-10-27
File: main.py
License: MIT
"""

from src.bitcoin import BitCoin
from src.credit_card import CreditCard
from src.debit_card import DebitCard
from src.interfaces.payment import Payment


def main() -> None:
    """
    Initializes and processes a batch of diverse payment types.
    """
    # Professional type hint using square brackets for collections
    payments: list[tuple[Payment, float]] = [
        (BitCoin(), 4000.0),
        (CreditCard(), 1000.0),
        (DebitCard(), 2000.0)
    ]

    for payment, amount in payments:
        payment.process(amount)


if __name__ == '__main__':
    main()

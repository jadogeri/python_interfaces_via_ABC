"""
Payment System - Credit Card Implementation
-------------------------------------------
Description: Concrete implementation of the Payment protocol for 
             Credit Card transactions.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2023-10-27
File: credit_card.py
License: MIT
"""

from app.src.interfaces.payment import Payment

class CreditCard(Payment):
    """Handles Credit Card payment processing logic."""

    def process(self, amount: float) -> None:
        """
        Processes a Credit Card transaction.

        Args:
            amount (float): The total amount to be processed.
        """
        print(f"Processing {amount} Credit Card...")

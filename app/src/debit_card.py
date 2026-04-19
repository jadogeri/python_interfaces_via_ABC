"""
Payment System - Debit Card Implementation
------------------------------------------
Description: Concrete implementation of the Payment protocol for 
             Debit Card transactions.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2023-10-27
File: debit_card.py
License: MIT
"""

from app.src.interfaces.payment import Payment

class DebitCard(Payment):
    """Handles Debit Card payment processing logic."""

    def process(self, amount: float) -> None:
        """
        Processes a Debit Card transaction.

        Args:
            amount (float): The total amount to be processed.
        """
        print(f"Processing {amount} Debit Card...")

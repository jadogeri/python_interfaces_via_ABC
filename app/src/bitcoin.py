"""
Payment System - Bitcoin Implementation
---------------------------------------
Description: Concrete implementation of the Payment protocol for 
             Bitcoin transactions.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2023-10-27
File: bitcoin.py
License: MIT
"""

from app.src.interfaces.payment import Payment


class BitCoin(Payment):
    """Handles Bitcoin payment processing logic."""

    def process(self, amount: float) -> None:
        """
        Processes a Bitcoin transaction.

        Args:
            amount (float): The total amount to be processed in BTC.
        """
        print(f"Processing {amount} BTC...")

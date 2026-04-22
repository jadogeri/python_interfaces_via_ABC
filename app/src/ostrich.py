"""
Payment System - Ostrich Implementation
---------------------------------------
Description: Concrete implementation of the Bird interface for 
             Ostrich behavior.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2026-04-27
File: ostrich.py
License: MIT
"""

from src.interfaces.bird import Bird
class Ostrich(Bird):

    """Handles Ostrich behavior logic."""
    def eat(self):
        return "Ostrich eats plants."
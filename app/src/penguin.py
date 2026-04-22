"""
Payment System - Penguin Implementation
---------------------------------------
Description: Concrete implementation of the Bird and Swimable interfaces for 
             Penguin behavior.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2026-04-27
File: penguin.py
License: MIT
"""

from app.src.interfaces.bird import Bird
from app.src.interfaces.swimmable import Swimmable
class Penguin(Bird, Swimmable):

    def swim(self):
        """Implements the swim behavior for the Penguin."""
        return "Penguin swims gracefully in the water."

        """Implements the eat behavior for the Penguin."""
    def eat(self):
        return "Penguin eats fish."
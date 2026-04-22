"""
Payment System - Eagle Implementation
---------------------------------------
Description: Concrete implementation of the Bird and Flyable interfaces for 
             Eagle behavior.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2026-04-27
File: eagle.py
License: MIT
"""

from src.interfaces.bird import Bird
from src.interfaces.flyable import Flyable
class Eagle(Bird, Flyable):

    def fly(self):
        """Implements the fly behavior for the Eagle."""
        return "Eagle soars high in the sky.";

        """Implements the eat behavior for the Eagle."""
    def eat(self):
        return "Eagle eats small mammals."
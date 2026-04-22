"""
Payment System - Flyable Interface
---------------------------------------
Description: Defines the Flyable interface with essential behaviors.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2026-04-27
File: flyable.py
License: MIT
"""




from abc import ABC, abstractmethod

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


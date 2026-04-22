"""
Payment System - Swimmable Interface
---------------------------------------
Description: Defines the Swimmable interface with essential behaviors.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2026-04-27
File: swimmable.py
License: MIT
"""




from abc import ABC, abstractmethod 

class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass

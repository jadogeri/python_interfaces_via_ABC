"""
Payment System - Bird Interface
---------------------------------------
Description: Defines the Bird interface with essential behaviors.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2026-04-27
File: bird.py
License: MIT
"""


from abc import ABC, abstractmethod
class Bird(ABC):
    @abstractmethod
    def eat(self):
        pass

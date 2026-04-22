"""
Birds - Entry Point
----------------------------
Description: Orchestrates the execution of different bird behaviors
             using the Bird, Flyable, and Swimmable ABC interfaces.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2023-10-27
File: main.py
License: MIT
"""

from src.penguin import Penguin
from src.eagle import Eagle
from src.ostrich import Ostrich
from src.interfaces.bird import Bird
from src.interfaces.swimmable import Swimmable
from src.interfaces.flyable import Flyable


def main() -> None:
    """
    Initializes and processes a batch of diverse bird types, 
    dynamically checking for flyable and swimmable capabilities.
    """
    # Professional type hint for the list of bird instances
    birds: list[Bird] = [
        Penguin(),
        Eagle(),
        Ostrich()
    ]

    print("--- Bird Behavior Simulation ---")

    for bird in birds:
        # Every bird can eat
        print(f"\n{bird.__class__.__name__}:")
        print(f"  - Food: {bird.eat()}")

        # Check for Swimmable capability
        if isinstance(bird, Swimmable):
            print(f"  - Water: {bird.swim()}")
        
        # Check for Flyable capability
        if isinstance(bird, Flyable):
            print(f"  - Air: {bird.fly()}")


if __name__ == '__main__':
    main()

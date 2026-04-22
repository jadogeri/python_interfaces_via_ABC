"""
Bird System Unit Tests
---------------------
Description: Validates behavioral logic for Eagle, Penguin, and Ostrich
             using ABC-based interfaces.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2023-10-27
File: tests.py
License: MIT
"""

import unittest
from src.interfaces.bird import Bird
from src.interfaces.flyable import Flyable
from src.interfaces.swimmable import Swimmable
from src.eagle import Eagle
from src.penguin import Penguin
from src.ostrich import Ostrich

class BirdTest(unittest.TestCase):

    def setUp(self):
        print("SETUP called ...")
        self.eagle = Eagle()
        self.penguin = Penguin()
        self.ostrich = Ostrich()

    def tearDown(self):
        print("TEARDOWN called ...")

    # 1-3. Test Eating Behaviors (Matching your specific return strings)
    def test_eagle_eat(self):
        self.assertEqual(self.eagle.eat(), "Eagle eats small mammals.")

    def test_penguin_eat(self):
        self.assertEqual(self.penguin.eat(), "Penguin eats fish.")

    def test_ostrich_eat(self):
        self.assertEqual(self.ostrich.eat(), "Ostrich eats plants.")

    # 4-5. Test Movement Behaviors
    def test_eagle_fly(self):
        self.assertEqual(self.eagle.fly(), "Eagle soars high in the sky.")

    def test_penguin_swim(self):
        self.assertEqual(self.penguin.swim(), "Penguin swims gracefully in the water.")

    # 6-8. Interface Compliance
    def test_eagle_interfaces(self):
        self.assertIsInstance(self.eagle, Bird)
        self.assertIsInstance(self.eagle, Flyable)

    def test_penguin_interfaces(self):
        self.assertIsInstance(self.penguin, Bird)
        self.assertIsInstance(self.penguin, Swimmable)
        self.assertNotIsInstance(self.penguin, Flyable)

    def test_ostrich_interfaces(self):
        self.assertIsInstance(self.ostrich, Bird)
        self.assertNotIsInstance(self.ostrich, Flyable)

    # 9. Test Abstract Enforcement
    def test_cannot_instantiate_abc(self):
        with self.assertRaises(TypeError):
            Bird()

    # 10. Bulk SubTest loop
    def test_all_birds_eat_logic(self):
        """Validates all bird eat strings in one batch"""
        cases = [
            (self.eagle, "Eagle eats small mammals."),
            (self.penguin, "Penguin eats fish."),
            (self.ostrich, "Ostrich eats plants."),
        ]
        for bird_obj, expected in cases:
            with self.subTest(bird=type(bird_obj).__name__):
                self.assertEqual(bird_obj.eat(), expected)

if __name__ == "__main__":
    unittest.main()

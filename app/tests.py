"""
Bird System Unit Tests
---------------------
Description: Validates the behavioral logic for various bird implementations
             using ABC-based interfaces (Flyable, Swimmable).

Author: Joseph Adogeri
Version: 1.0.0
Since: 2024-05-20
File: test_birds.py
License: MIT
"""

import unittest
from app.src.penguin import Penguin
from app.src.eagle import Eagle
from app.src.ostrich import Ostrich
from app.src.interfaces.flyable import Flyable

# --- Unit Tests ---

class BirdTest(unittest.TestCase):

    def setUp(self):
        """Initialize instances for testing"""
        self.eagle = Eagle()
        self.penguin = Penguin()
        self.ostrich = Ostrich()

    def tearDown(self):
        """Cleanup after tests"""
        pass

    # 1-3. Test Eating Behaviors
    def test_eagle_eat(self):
        self.assertEqual(self.eagle.eat(), "Eagle eats small mammals.")

    def test_penguin_eat(self):
        self.assertEqual(self.penguin.eat(), "Penguin eats fish.")

    def test_ostrich_eat(self):
        self.assertEqual(self.ostrich.eat(), "Ostrich eats seeds.")

    # 4-5. Test Movement Behaviors
    def test_eagle_fly(self):
        self.assertEqual(self.eagle.fly(), "Eagle soars high.")

    def test_penguin_swim(self):
        self.assertEqual(self.penguin.swim(), "Penguin swims in cold water.")

    # 6-8. Test Interface Compliance (isinstance)
    def test_eagle_interfaces(self):
        self.assertTrue(isinstance(self.eagle, Flyable))
        self.assertTrue(isinstance(self.eagle, Bird))

    def test_penguin_interfaces(self):
        self.assertTrue(isinstance(self.penguin, Swimmable))
        self.assertFalse(isinstance(self.penguin, Flyable))

    def test_ostrich_interfaces(self):
        self.assertTrue(isinstance(self.ostrich, Bird))
        self.assertFalse(isinstance(self.ostrich, Flyable))
        self.assertFalse(isinstance(self.ostrich, Swimmable))

    # 9. Test Abstract Enforcement (Cannot instantiate ABC directly)
    def test_cannot_instantiate_abc(self):
        with self.assertRaises(TypeError):
            Bird()

    # 10. Data-Driven SubTest (Similar to your example)
    def test_all_birds_eat_logic(self):
        """Loop through cases to ensure all bird types have specific eat outputs"""
        cases = [
            (self.eagle, "Eagle eats small mammals."),
            (self.penguin, "Penguin eats fish."),
            (self.ostrich, "Ostrich eats seeds."),
        ]
        for bird_obj, expected in cases:
            with self.subTest(bird=type(bird_obj).__name__):
                self.assertEqual(bird_obj.eat(), expected)

if __name__ == "__main__":
    unittest.main()

import unittest
from io import StringIO
from unittest.mock import patch

# Standard imports now work because pyproject.toml defines the pythonpath
from app.src.bitcoin import BitCoin
from app.src.credit_card import CreditCard
from app.src.debit_card import DebitCard
from app.src.interfaces.payment import Payment


class PaymentTest(unittest.TestCase):

    def setUp(self):
        print("SETUP called ...")
        # Define our test cases: (Object, Amount, Expected String)
        self.cases: list[tuple[Payment, float, str]] = [
            (BitCoin(), 4000.0, "Processing 4000.0 BTC..."),
            (CreditCard(), 1000.0, "Processing 1000.0 Credit Card..."),
            (DebitCard(), 2000.0, "Processing 2000.0 Debit Card..."),
        ]

    def tearDown(self):
        print("TEARDOWN called ...")
        self.cases = []

    def test_all_payments(self):
        """Tests all payment types inside a single class method"""
        for payment_obj, amount, expected_output in self.cases:
            # 'subTest' allows the loop to continue even if one case fails
            with self.subTest(payment=type(payment_obj).__name__):
                with patch('sys.stdout', new=StringIO()) as fake_out:
                    payment_obj.process(amount)
                    self.assertEqual(fake_out.getvalue().strip(), expected_output)

if __name__ == "__main__":
    unittest.main()

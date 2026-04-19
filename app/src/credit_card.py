from app.src.interfaces.payment import Payment

class CreditCard(Payment):
    def process(self, amount: float) -> None:
        print(f"Processing {amount} Credit Card...")
from app.src.interfaces.payment import Payment

class DebitCard(Payment):
    def process(self, amount: float) -> None:
        print(f"Processing {amount} Debit Card...")
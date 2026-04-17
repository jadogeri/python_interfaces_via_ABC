from src.interfaces.payment import Payment

class BitCoin(Payment):
    def process(self, amount: float) -> None:
        print(f"Processing {amount} BTC...")
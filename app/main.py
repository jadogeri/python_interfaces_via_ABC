from src.bitcoin import BitCoin
from src.credit_card import CreditCard
from src.debit_card import DebitCard
from src.interfaces.payment import Payment


def main()-> None:
    payments: list[tuple(Payment, float)]  = [
        (BitCoin(), 4000),
        (CreditCard(), 1000),
        (DebitCard(), 2000)
    ]

    ''' Loop through all payments '''
    for payment,amount in payments:
        payment.process(amount);


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main();


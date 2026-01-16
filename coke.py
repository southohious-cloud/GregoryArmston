"""
coke.py — Logic and main program for a coin-operated Coke machine.
"""

VALID_COINS = {25, 10, 5}
PRICE = 50

def process_coin(coin: int, amount_due: int) -> int:
    """
    Process a single coin and return the updated amount due.
    Only valid coins (25, 10, 5) reduce the amount due.
    """
    if coin in VALID_COINS:
        amount_due -= coin
    return amount_due

def main():
    amount_due = PRICE

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            continue

        amount_due = process_coin(coin, amount_due)

    print(f"Change Owed: {abs(amount_due)}")

if __name__ == "__main__":
    main()


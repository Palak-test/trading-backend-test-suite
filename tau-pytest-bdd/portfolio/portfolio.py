"""
This module models a simple trading portfolio with positions and cash balance.
"""

class Portfolio:
    def __init__(self, cash=10000):
        self.cash = cash
        self.positions = {}

    def buy(self, symbol, quantity, price):
        cost = quantity * price
        if self.cash < cost:
            raise ValueError("Insufficient cash to buy.")
        self.cash -= cost
        self.positions[symbol] = self.positions.get(symbol, 0) + quantity

    def sell(self, symbol, quantity, price):
        if self.positions.get(symbol, 0) < quantity:
            raise ValueError("Not enough shares to sell.")
        self.positions[symbol] -= quantity
        self.cash += quantity * price
        if self.positions[symbol] == 0:
            del self.positions[symbol]

    def get_position(self, symbol):
        return self.positions.get(symbol, 0)

    def get_cash(self):
        return self.cash

class Ledger:

    def __init__(self):

        self.items = []

    def add(self, transaction):

        self.items.append(transaction)

    def all(self):

        return self.items

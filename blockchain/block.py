from time import time

from utility.printable import Printable

class Block(Printable):
    """A single block of our blockchain."""
    def __init__(self, index, previous_hash, transactions, proof, time=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time
        self.transactions = transactions
        self.proof = proof



# 1. Create a Blockchain class whose constructor creates an empty list (to store our blockchain)
# and another to store transactions.
# this Blockchain class is responsible for managing the chain.
# it will store transactions and have some helper methods
# for adding new blocks to the chain
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []]

    def block_new(self):
        # creates a new Block and adds it to the chain pass

    def transaction_new(self):
        # adds a new transaction to the list of transactions pass

    @staticmethod
    def hash(block):
        # hashes a block pass

    @property
    def block_last(selfself):
        # returns the last Block in teh chain pass
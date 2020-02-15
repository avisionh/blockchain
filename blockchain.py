# 1. Create a Blockchain class whose constructor creates an empty list (to store our blockchain)
# and another to store transactions.
# this Blockchain class is responsible for managing the chain.
# it will store transactions and have some helper methods
# for adding new blocks to the chain
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def block_new(self):
        # creates a new Block and adds it to the chain pass

    def transaction_new(self, sender, recipient, amount):
        # adds a new transaction to the list of transactions passed
        """
        creates a new transaction to go into the next mined block
        :param sender: <str> address of the sender
        :param recipient: <str> address of the recipient
        :param amount: <int> amount passed from transaction
        :return: <int> the index of the block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # hashes a block pass
        pass

    @property
    def block_last(selfself):
        # returns the last Block in teh chain pass
        pass
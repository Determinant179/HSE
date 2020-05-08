import random

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
    
def data_generate():
    sender_number = random.randint(1, 62)
    recipient_number = random.randint(1, 62)

    while recipient_number == sender_number:
        recipient_number = random.randint(1, 62)

    with open("nickname_base.txt", "r") as f:
        for i in range(sender_number):
            f.readline()
        sender = f.readline()

    with open("nickname_base.txt", "r") as f:
        for i in range(recipient_number):
            f.readline()
        recipient = f.readline()

    amount = random.randint(1, 100)

    return [sender[:len(sender) - 1], recipient[:len(recipient) - 1], amount]

def transaction_generate():
    data = data_generate()
    return Transaction(data[0], data[1], data[2])

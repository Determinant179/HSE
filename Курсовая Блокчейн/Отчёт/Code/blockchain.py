import hash_function
import transaction_info
import datetime
import PoW_function as PoW

class Block:
    def __init__(self, counter, time, data, previous_hash):
        self.counter = counter
        self.time = time
        self.data = transaction_info.transaction_generate()
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
    
    def hash_block(self):
        return hash_function.hasher(str(self.counter) + str(self.time) + self.data.sender + self.data.recipient + str(self.data.amount) + self.previous_hash)

def create_genesis_block():
    return Block(1, datetime.datetime.now(), "Genesis Block", "")

def new_block(last_block):
    i = 0
    while not PoW.PoW(i, last_block.counter):
        i += 1
    this_counter = last_block.counter + 1
    this_time = datetime.datetime.now()
    this_data = last_block.data.sender + " send " + str(last_block.data.amount) + " COINs to " + last_block.data.recipient
    this_hash = last_block.hash
    return Block(this_counter, this_time, this_data, this_hash)

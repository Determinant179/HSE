import blockchain as bc

blockchain = [bc.create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks = 30

for i in range(0, num_of_blocks):
    current_block = bc.new_block(previous_block)
    blockchain.append(current_block)
    previous_block = current_block

    print("Block " + str(current_block.counter) + " has been added\n")
    print("Transactoin info:")
    print("Sender - " + current_block.data.sender)
    print("Recipient - " + current_block.data.recipient)
    print("Amount of transaction - " + str(current_block.data.amount))
    print("\nHash - " + current_block.hash + "\n\n\n")
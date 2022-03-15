import hashlib

class Block:
    def __init__(self, previous_block, block_array):
        self.previous_block =previous_block
        self.block_array = block_array
        self.block_data = "-".join(self.block_array) + "-" + self.previous_block
        self.hash_block = hashlib.sha256(self.block_data.encode()).hexdigest()

genesis_block = 'nftx-24r'
transaction_1 = 'xx0-tranx01'
transaction_2 = 'nft-tranx02'
transaction_3 = 'nft-tranx03'
transaction_4 = 'nft-tranx04'
transaction_5 = 'nft-tranx05'
transaction_6 = 'nft-tranx67'
block1 = Block(genesis_block, [transaction_1, transaction_2])
print(block1.block_data)
print(block1.hash_block)
block2 = Block(block1.hash_block, [transaction_3, transaction_4])
print(block2.hash_block)
block3 = Block(block1.hash_block, [transaction_5, transaction_6])
print(block3.hash_block)
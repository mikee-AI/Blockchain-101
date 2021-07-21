# import hashlib

ledger = [
			" X0 sent 2.3 VC to X3 ", 
			" X2 sent 3.1 VC to X1 ",
			" X3 sent 0.7 VC to X0 ",
			" X1 sent 1.8 VC to X2 ",
			" X0 sent 9.2 VC to X1 ",
			" X2 sent 4.5 VC to X0 ",
		 ]


from hashlib import sha256
import json 
from datetime import datetime as dt 

class Block:
    def __init__(self, blockNumber, transactions, prevHash, 
                 nonce=0000, timestamp=str(dt.now())):
        self.blockNumber = blockNumber
        self.nonce = nonce
        self.timestamp = timestamp
        self.transactions = transactions       
        self.prevHash = prevHash
        self.blockData = json.dumps(self.__dict__, sort_keys=True, indent=4)
        
    def hash(self):
        blockHash = sha256(self.blockData.encode()).hexdigest()
        return blockHash
 
genesisBlock = Block(0, ledger[0:2], "hdahsfdjh45bafsk")


print(genesisBlock.hash())




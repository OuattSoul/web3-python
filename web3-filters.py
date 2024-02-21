from web3 import Web3
from datetime import datetime

# Defining url for collecting ETH transactions
infura_url = "https://mainnet.infura.io/v3/API_KEY"

# Making connections with infra url
web3 = Web3(Web3.HTTPProvider(infura_url))
print("Connection is successful:", web3.isConnected())


# Wallet Address
account = "0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f"
# Checking the balance for that address (in WEIs)
try:
    print("Input Address:", account)
    balance = web3.eth.getBalance(account)
except:
    # If its not a lowercase()
    account = Web3.toChecksumAddress(account)
    print("Input Address:", account)
    balance = web3.eth.getBalance(account)

# Print balance in WEIs
print("Balance in WEIs:", balance)

# Converting account balance to ETH
balanceWEI = web3.fromWei(balance, "ether")
print("Balance in ETH:", balanceWEI)


# Defining start block and latest block
start_block = web3.eth.blockNumber-5000
end_block = web3.eth.blockNumber


for block_num in range(start_block, end_block):

    current_block = block_num

    # Get block with specific number with all transactions
    block = web3.eth.getBlock(block_num, full_transactions=True)

    list_of_block_transactions = block.transactions
    for transaction in list_of_block_transactions:

        to_account = transaction['to']
        from_account = transaction['from']

        if to_account == account:
            print("To account:", to_account)         
            to_match = True
        else:
            to_match = False            


        if from_account == account:
            print("From account:", from_account)
            from_account = True
            
        else:
            from_account = False            

    
        if to_match == True or from_account == True:
            print("Found Transaction with HASH:", transaction['hash'])
            print("Found Transaction with HASH-HEX:", transaction['hash'].hex())
            print("Found Transaction with value:", transaction['value']) 
            print("Found Transaction with gas:", transaction['gas']) 
            
            print()

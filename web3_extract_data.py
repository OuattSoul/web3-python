from web3 import Web3

# Initialisation de l'objet Web3
infura_url = ""
web3 = Web3(Web3.HTTPProvider(infura_url))

# 0x634438d879a90a25437B87168252c2b983734391

def get_transactions(address):
    transactions = []

    # obtenir le nonce
    nonce = web3.eth.get_transaction_count(address)

    #  starting block
    start = 14227989
    end = 17620210
    # Récupération des transactions
    for i in range(start,end):
        blockTx = web3.eth.get_block(i,True).transactions
        # print(tx_hash)

        for transaction in blockTx:
            if transaction['to'] == address or transaction['from'] == address:
            # transaction = web3.eth.get_transaction(tx)
                print("Transaction hash:", transaction["hash"].hex())
                print("From:", transaction["from"])
                print("To:", transaction["to"])
                print("Value:", transaction["value"])
                print("\n")
            # if transaction["to"] == address or transaction["from"] == address:
            #     transactions.append(transaction)

    return transactions


address = input("Entrez l'adresse : ")

get_transactions(address)

# Affichage des transactions
# for tx in transactions:
#     print("Transaction hash:", tx["hash"].hex())
#     print("From:", tx["from"])
#     print("To:", tx["to"])
#     print("Value:", tx["value"])
#     print("\n")

# for tx in transactions:
#     print(tx)

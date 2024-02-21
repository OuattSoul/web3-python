from web3 import Web3
# from datetime import datetime
import datetime
# Initialisation de l'objet Web3
infura_url = "https://mainnet.infura.io/v3/API_KEY"
web3 = Web3(Web3.HTTPProvider(infura_url))


debut = 160000
fin = web3.eth.block_number


# for i in range(debut,fin):
#     print(i)

block_time = web3.eth.get_block(17621192).timestamp
print(block_time)

# date_time = datetime.fromtimestamp(block_time)
# print("Date Format : ", date_time)

# assigned regular string date
start_date = [datetime.datetime(2022, 4, 1, 8, 00), datetime.datetime(2022, 4, 1, 8, 30)]
end_date = [datetime.datetime(2022, 4, 30, 8, 00),datetime.datetime(2022, 4, 30, 8, 30)]

# print regular python date&time
print("start_date =>",start_date)

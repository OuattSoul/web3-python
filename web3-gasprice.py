from web3 import Web3
import json
import requests

# https://ethgasstation.info/

alchemy_http = 'https://eth-mainnet.alchemyapi.io/v2/API_KEY'
web3 = Web3(Web3.HTTPProvider(alchemy_http))

req = requests.get('https://ethgasstation.info/json/ethgasAPI.json')
t = json.loads(req.content)
print('safeLow', t['safeLow'])
print('average', t['average'])
print('fast', t['fast'])
print('fastest', t['fastest'])


#web3.eth.Eth.generateGasPrice`
gas_price1 = web3.eth.gasPrice
print(gas_price1/10**8)

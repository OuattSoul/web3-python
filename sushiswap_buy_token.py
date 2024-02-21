from decimal import Decimal
from distutils.command.config import config
from web3 import Web3
import time
import config
import uniSwapABI

alchemy_http = "https://eth-rinkeby.alchemyapi.io/v2/API_KEY"


web3 = Web3(Web3.HTTPProvider(alchemy_http))

print(web3.isConnected())

# sushirouterContractAddress = '0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F' # sushiswap contract address on mainnet 

sushirouterContractAddress = '0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506' # sushiswap contract address on rinkeby testnet 

# sushirouterContractAddress = '0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984'

#uniABI = uniSwapABI.uniABI

# wallet_address = input('Enter the receiver wallet public address : ')

wallet_address = config.WALLET_ADDRESS

contract  = web3.eth.contract(address = sushirouterContractAddress, abi = uniSwapABI.uniABI)

sellABI = '[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint8","name":"_decimals","type":"uint8"},{"internalType":"uint256","name":"supply","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'

tokenToBuy = web3.toChecksumAddress(input("Enter the Token Address you want to buy : ")) 

sellTokenContract = web3.eth.contract(tokenToBuy, abi = sellABI)


balance = web3.eth.getBalance(wallet_address)
print(balance)
readeable_balance = web3.fromWei(balance, 'ether')
print(readeable_balance, "ETH")


# get token balance

tokenBalance = sellTokenContract.functions.balanceOf(wallet_address).call()
tokenSymbol = sellTokenContract.functions.symbol().call()
readeable_token_balance = web3.fromWei(tokenBalance, 'ether')
print("Your actual Token Balance is : " + str('%.18f' % Decimal(readeable_token_balance)) + " " + tokenSymbol)

# tokenToBuy = web3.toChecksumAddress(input("Enter the Token Address you want to buy : "))  # 0xf5f06fFa53Ad7F5914F493F16E57B56C8dd2eA80 jelly

# tokenToBuy = web3.toChecksumAddress(input("Enter the Token Address you want to buy : ")) 
# 0xc7AD46e0b8a400Bb3C915120d284AafbA8fc4735  DAI rinkeby 
# 0x4DBCdF9B62e891a7cec5A2568C3F4FAF9E8Abe2b USD Coin

# 0x01BE23585060835E02B77ef475b0Cc51aA1e0709 LINK
# 0x93341222b303992e553Bb5A9aaf66BCA9b9E12Cf TOR Token
# 0x34270631F44C24fc320283347c38515798fA4388 Mocked DAI
# 0x4DBCdF9B62e891a7cec5A2568C3F4FAF9E8Abe2b USD Coin


# sellABI = input('Enter the Token ABI that you want to buy : ')
# buyTokenContract = web3.eth.contract(tokenToBuy, abi = '{sellABI}')
# token_balance = buyTokenContract.functions.balanceOf(wallet_address).call()
# readeable_token_balance= Web3.fromWei(token_balance, 'ether')
# token_symbol = buyTokenContract.functions.symbol().call()
# print(f' Your wallet address has actually : {readeable_token_balance} {token_symbol} ')

wrapped_address = web3.toChecksumAddress("0xc778417e063141139fce010982780140aa0cd5ab") # weth address on testnet

nonce = web3.eth.getTransactionCount(wallet_address)

start = time.time()

amountIn = 0

value= 0.1

gas_price = '15'

nonce2 = 0
# Buying process

def BuyingProcess():

    tokenBalance = sellTokenContract.functions.balanceOf(wallet_address).call()
    tokenSymbol = sellTokenContract.functions.symbol().call()
    readeable_token_balance = web3.fromWei(tokenBalance, 'ether')
    print("Your actual Token Balance is : " + str('%.18f' % Decimal(readeable_token_balance)) + " " + tokenSymbol)

    uniSwap_tx = contract.functions.swapExactETHForTokens(
        0,
        [wrapped_address, tokenToBuy],
        wallet_address,
        (int(time.time()) + 10000)
    ).buildTransaction({
        'from': wallet_address,
        'value': web3.toWei(value, 'ether'),
        'gas': 300000,
        'gasPrice': web3.toWei('20', 'gwei'),
        'nonce': nonce,
    })

    # Sign & send the transaction that is the buying transaction
    signedTx = web3.eth.account.sign_transaction(uniSwap_tx, private_key = config.PRIVATE_KEY)
    tx_token = web3.eth.send_raw_transaction(signedTx.rawTransaction)
    print('Transaction Hash : ',web3.toHex(tx_token))

    time.sleep(12)
    
    tokenBalance = sellTokenContract.functions.balanceOf(wallet_address).call()
    tokenSymbol = sellTokenContract.functions.symbol().call()
    readeable_token_balance = web3.fromWei(tokenBalance, 'ether')
    print("Your actual Token Balance is : " + str('%.18f' % Decimal(readeable_token_balance)) + " " + tokenSymbol)

    # print(f' Your wallet address has : {readeable_token_balance} {token_symbol} after buying')


if __name__ == '__main__':
    BuyingProcess()

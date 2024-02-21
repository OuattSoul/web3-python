from distutils.command.config import config
from web3 import Web3
import json
import time
import config
import uniSwapABI
from decimal import Decimal


alchemy_http = "https://eth-goerli.g.alchemy.com/v2/API_KEY"

web3 = Web3(Web3.HTTPProvider(alchemy_http))

print(web3.isConnected())

uniRouterContractAddress = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D' # uniswap contract address on testnet 

wallet_address = config.WALLET_ADDRESS

spend = web3.toChecksumAddress("0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6") # weth address on testnet

value= 0.1

balance = web3.eth.getBalance(wallet_address)
#print(balance)
readeable_balance = web3.fromWei(balance, 'ether')
print('Actual Balance is : ',readeable_balance, "ETH")

wrapped = web3.toChecksumAddress("0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6")
tokenToSell = web3.toChecksumAddress(input("Enter the Token Address you want to sell : ")) # 0xaD6Db97C844Ec7Bb4c0641d436AA0D395fDD3f45 DAI Token [MOCK] 
tokenOutput = web3.toChecksumAddress(input("Enter the Token Address you want to get : ")) # 0x3BB0BeF1B70F8698bDaCb469F53980E30d9304d9 USDT

contract  = web3.eth.contract(address = uniRouterContractAddress, abi = uniSwapABI.uniABI)

sellABI = '[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint8","name":"_decimals","type":"uint8"},{"internalType":"uint256","name":"supply","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'

sellTokenContract = web3.eth.contract(tokenToSell, abi = sellABI)

# Get Token Balance
tokenBalance = sellTokenContract.functions.balanceOf(wallet_address).call()
tokenSymbol = sellTokenContract.functions.symbol().call()
readeable_token_balance = web3.fromWei(tokenBalance, 'ether')
print("Balance is : " + str('%.18f' % Decimal(readeable_token_balance)) + " " + tokenSymbol)
print("Balance == ", tokenBalance)

# test = input("stop")
percentage = 0.5 # 50% 
readeable_balance_decimal = str('%.18f' % Decimal(readeable_token_balance))
# sell_token_value = web3.toWei(input("Enter the value of " + tokenSymbol + " you want to sell : "), 'ether')
sell_token_value = web3.toWei(readeable_token_balance, 'ether')

sell_token_value_ether = web3.fromWei(sell_token_value, 'ether')

# The amount of input tokens to send.
amount = input("Enter the amount you want to sell : ")
amountIn = web3.toWei(amount, "ether")

# The minimum amount of output tokens that must be received
amountOutMin = web3.toWei("0.0001", "ether")
print('amountIn :', amountIn)
print('amountIn type :', type(amountIn))

start = time.time()

def SellingProcess():

    token_approve = sellTokenContract.functions.approve(uniRouterContractAddress, tokenBalance).buildTransaction({
        'from': wallet_address,
        'gasPrice': web3.toWei('80', 'gwei'),
        'gas': 300000,
        # 'gas': web3.fromWei(15000000000, 'ether'),
        'nonce': web3.eth.getTransactionCount(wallet_address),
    })

    signedTx = web3.eth.account.sign_transaction(token_approve, private_key = config.PRIVATE_KEY)
    tx_token = web3.eth.send_raw_transaction(signedTx.rawTransaction)
    print("Approved : " + web3.toHex(tx_token))

    time.sleep(60)

    print(f"Swapping {readeable_balance_decimal} {tokenSymbol} for ETH")

    pancakeSwap_tx = contract.functions.swapExactTokensForTokens(
        amountIn,
        0,
        [tokenToSell, tokenOutput],
        wallet_address,
        (int(time.time()) + 1000000)
    ).buildTransaction({
        'from': wallet_address,
        # 'value': web3.toWei(value, 'ether'),
        'gas': 500000,
        # 'gas': web3.fromWei(15000000000, 'ether'),
        'gasPrice': web3.toWei('140', 'gwei'),
        'nonce': web3.eth.getTransactionCount(wallet_address) + 1,
    })

    signedTxn = web3.eth.account.sign_transaction(pancakeSwap_tx, private_key = config.PRIVATE_KEY)
    txn_token = web3.eth.send_raw_transaction(signedTxn.rawTransaction)
    print(f"Sold {tokenSymbol} " + web3.toHex(txn_token))




if __name__ == '__main__':
    SellingProcess()

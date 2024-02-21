# from distutils.command.config import config
import math
from web3 import Web3
import time
import config
import uniSwapABI
from decimal import Decimal


alchemy_http = "https://eth-rinkeby.alchemyapi.io/v2/API_KEY"



web3 = Web3(Web3.HTTPProvider(alchemy_http))

print(web3.isConnected())

uniRouterContractAddress = '0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506' # sushiswap contract address on testnet 

wallet_address = config.WALLET_ADDRESS

spend = web3.toChecksumAddress("0xc778417e063141139fce010982780140aa0cd5ab") # weth address on testnet

balance = web3.eth.getBalance(wallet_address)
#print(balance)
readeable_balance = web3.fromWei(balance, 'ether')
print('Actual Balance is : ',readeable_balance, "ETH")

#tokenToSell = web3.toChecksumAddress("0xc7AD46e0b8a400Bb3C915120d284AafbA8fc4735")
tokenToSell = web3.toChecksumAddress(input("Enter the Token Address you want to sell : ")) #0xc7AD46e0b8a400Bb3C915120d284AafbA8fc4735 DAI Token on testnet

# 0xc7AD46e0b8a400Bb3C915120d284AafbA8fc4735  DAI rinkeby 
# 0x4DBCdF9B62e891a7cec5A2568C3F4FAF9E8Abe2b USD Coin

# 0x01BE23585060835E02B77ef475b0Cc51aA1e0709 LINK
# 0x93341222b303992e553Bb5A9aaf66BCA9b9E12Cf TOR Token
# 0x34270631F44C24fc320283347c38515798fA4388 Mocked DAI
# 0x4DBCdF9B62e891a7cec5A2568C3F4FAF9E8Abe2b USD Coin

contract  = web3.eth.contract(address = uniRouterContractAddress, abi = uniSwapABI.uniABI)

sellABI = '[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint8","name":"_decimals","type":"uint8"},{"internalType":"uint256","name":"supply","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'

#spend = web3.toChecksumAddress("0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c") # wbnb address 
sellTokenContract = web3.eth.contract(tokenToSell, abi = sellABI)

# Get Token Balance
tokenBalance = sellTokenContract.functions.balanceOf(wallet_address).call()
tokenSymbol = sellTokenContract.functions.symbol().call()
tokenDecimals = sellTokenContract.functions.decimals().call()
print('token decimals : ', tokenDecimals)

if(tokenDecimals == 18):
    readeable_token_balance = web3.fromWei(tokenBalance, 'ether')
    print("Your Token " + tokenSymbol + " Balance in ETH is : " + str(readeable_token_balance) + ' ' + tokenSymbol)

   

    percentage = 0.5 # 50% 
    sell_token_value = web3.toWei(readeable_token_balance, 'ether')
    # sell_token_value_ether = web3.fromWei(sell_token_value, 'ether')
    sell_token_value_half = int(sell_token_value * percentage)
    print('sell_token_value_half :', sell_token_value_half)
    print('sell_token_value_half type :', type(sell_token_value_half))

    
    

elif(tokenDecimals == 15):
    readeable_token_balance = web3.fromWei(tokenBalance, 'kwei')
    print("Your Token " + tokenSymbol + " Balance in ETH is : " + str(readeable_token_balance) + ' ' + tokenSymbol)

    sell_token_value_trunc = round(readeable_token_balance,15)
    sell_token_value_str = str(sell_token_value_trunc)
    sell_token_value = Web3.toWei(sell_token_value_str, 'kwei')
    sell_token_value_ether = web3.fromWei(sell_token_value, 'kwei')

    print("You are going to sell this amount of your Token",sell_token_value_trunc, " ", tokenSymbol) 
    print('ether value : ', sell_token_value_ether)

    try:
        if(sell_token_value_trunc > 0):
            print('greater than 0')
    except Exception as e:
        print('less than 0', e)
        pass

elif(tokenDecimals == 12):
    readeable_token_balance = web3.fromWei(tokenBalance, 'mwei')
    print("Your Token " + tokenSymbol + " Balance in ETH is : " + str(readeable_token_balance) + ' ' + tokenSymbol)
    
    sell_token_value_trunc = round(readeable_token_balance,12)
    sell_token_value_str = str(sell_token_value_trunc)
    sell_token_value = Web3.toWei(sell_token_value_str, 'mwei')
    sell_token_value_ether = web3.fromWei(sell_token_value, 'mwei')

    print("You are going to sell this amount of your Token",sell_token_value_trunc, " ", tokenSymbol)
    print('ether value : ', sell_token_value_ether) 

    try:
        if(sell_token_value_trunc > 0):
            print('greater than 0')
    except Exception as e:
        print('less than 0', e)
        pass

elif(tokenDecimals == 9):
    readeable_token_balance = web3.fromWei(tokenBalance, 'gwei')
    print("Your Token " + tokenSymbol + " Balance in ETH is : " + str(readeable_token_balance) + ' ' + tokenSymbol)
    
    sell_token_value_trunc = round(readeable_token_balance,10)
    sell_token_value_str = str(sell_token_value_trunc)
    sell_token_value = Web3.toWei(sell_token_value_str, 'gwei')
    sell_token_value_ether = web3.fromWei(sell_token_value, 'gwei')

    print("You are going to sell this amount of your Token",sell_token_value_trunc, " ", tokenSymbol) 

    # sell_token_value = Web3.toWei(input("Enter the value of " + tokenSymbol + " you want to sell : "), 'ether')

    try:
        if(sell_token_value_ether >= readeable_token_balance):
            print('Tx possible')
    except Exception as e:
        print('Insufficient amount', e)
        pass

elif(tokenDecimals == 6):
    readeable_token_balance = web3.fromWei(tokenBalance, 'szabo')
    print("Your Token " + tokenSymbol + " Balance in ETH is : " + str(readeable_token_balance) + ' ' + tokenSymbol)
    
    sell_token_value_trunc = round(readeable_token_balance,6)
    sell_token_value_str = str(sell_token_value_trunc)
    sell_token_value = Web3.toWei(sell_token_value_str, 'gwei')
    sell_token_value_ether = web3.fromWei(sell_token_value, 'gwei')

    print("You are going to sell this amount of your Token",sell_token_value_trunc, " ", tokenSymbol)

    try:
        if(sell_token_value_trunc > 0):
            print('greater than 0')
    except Exception as e:
        print('less than 0', e)
        pass

elif(tokenDecimals == 3):
    readeable_token_balance = web3.fromWei(tokenBalance, 'finney')
    print("Your Token " + tokenSymbol + " Balance in ETH is : " + str(readeable_token_balance) + ' ' + tokenSymbol)
    
    sell_token_value_trunc = round(readeable_token_balance,3)
    sell_token_value_str = str(sell_token_value_trunc)
    sell_token_value = Web3.toWei(sell_token_value_str, 'finney')
    sell_token_value_ether = web3.fromWei(sell_token_value, 'finney')

    print("You are going to sell this amount of your Token",sell_token_value_trunc, " ", tokenSymbol)

    try:
        if(sell_token_value_trunc > 0):
            print('greater than 0')
    except Exception as e:
        print('less than 0', e)
        pass

start = time.time()
# print("You are going to sell this amount of your Token",sell_token_value, " ", tokenSymbol) 
# print("You are going to sell this amount of your Token",sell_token_value_exact, " ", tokenSymbol) 

token_approve = sellTokenContract.functions.approve(uniRouterContractAddress, tokenBalance).buildTransaction({
    'from': wallet_address,
    'gasPrice': web3.toWei('5', 'gwei'),
    'nonce': web3.eth.getTransactionCount(wallet_address),
})

signedTx = web3.eth.account.sign_transaction(token_approve, private_key = config.PRIVATE_KEY)
tx_token = web3.eth.send_raw_transaction(signedTx.rawTransaction)
print("Approved : " + web3.toHex(tx_token))

#after approve, wait for 10 sec before sending the tx
time.sleep(10)

# print(f"Swapping {sell_token_value_ether} {tokenSymbol} for ETH") 
print(f"Swapping {readeable_token_balance} {tokenSymbol} for ETH") 
# swap exact token for ETH

def SellingProcess():
    pancakeSwap_tx = contract.functions.swapExactTokensForETH(
        sell_token_value,
        0,
        [tokenToSell, spend],
        wallet_address,
        (int(time.time()) + 1000000)
    ).buildTransaction({
        'from': wallet_address,
        'gasPrice': web3.toWei('20', 'gwei'),
        'nonce': web3.eth.getTransactionCount(wallet_address),
    })

    signedTxn = web3.eth.account.sign_transaction(pancakeSwap_tx, private_key = config.PRIVATE_KEY)
    txn_token = web3.eth.send_raw_transaction(signedTxn.rawTransaction)
    print(f"Sold {tokenSymbol} " + web3.toHex(txn_token))
    # print("New Balance is : " + str(readeable_token_balance) + " " + tokenSymbol)
    # print('Your Token actual Balance is : ', readeable_balance)

if __name__== '__main__':
    SellingProcess()

from distutils.command.config import config
from web3 import Web3
import time
import config
import uniSwapABI

url = "https://eth-goerli.g.alchemy.com/v2/API_KEY"

web3 = Web3(Web3.HTTPProvider(url))

print(web3.isConnected())

uniRouterContractAddress = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D' # uniswap contract address on testnet 

# uniRouterContractAddress = '0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984'

#uniABI = uniSwapABI.uniABI

# wallet_address = input('Enter the receiver wallet public address : ')

wallet_address = config.WALLET_ADDRESS

balance = web3.eth.getBalance(wallet_address)
print(balance)
readeable_balance = web3.fromWei(balance, 'ether')
print(readeable_balance, "ETH")

contract  = web3.eth.contract(address = uniRouterContractAddress, abi = uniSwapABI.uniABI)

# 0xc7AD46e0b8a400Bb3C915120d284AafbA8fc4735  DAI rinkeby 
# 0x4DBCdF9B62e891a7cec5A2568C3F4FAF9E8Abe2b USD Coin

# 0x01BE23585060835E02B77ef475b0Cc51aA1e0709 LINK
# 0x93341222b303992e553Bb5A9aaf66BCA9b9E12Cf TOR Token
# 0x34270631F44C24fc320283347c38515798fA4388 Mocked DAI
# 0x4DBCdF9B62e891a7cec5A2568C3F4FAF9E8Abe2b USD Coin

tokenToSwap = web3.toChecksumAddress(input("Enter the Token Address you want to buy : ")) 

# sellABI = input('Enter the Token ABI that you want to buy : ')
# buyTokenContract = web3.eth.contract(tokenToSwap, abi = '{sellABI}')
# token_balance = buyTokenContract.functions.balanceOf(wallet_address).call()
# readeable_token_balance= Web3.fromWei(token_balance, 'ether')
# token_symbol = buyTokenContract.functions.symbol().call()
# print(f' Your wallet address has actually : {readeable_token_balance} {token_symbol} ')

wrapped_address = web3.toChecksumAddress("0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6") # weth address on testnet

nonce = web3.eth.getTransactionCount(wallet_address)

start = time.time()

amountIn = 0

value= 1

gas_price = '15'

amountOut = 300

nonce2 = 0
# Buying process
def BuyingProcess():
    uniSwap_tx = contract.functions.swapExactETHForTokens(
        0,
        [wrapped_address, tokenToSwap],
        wallet_address,
        (int(time.time()) + 10000)
    ).buildTransaction({
        'from': wallet_address,
        'value': web3.toWei(value, 'ether'),
        'gas': 300000,
        'gasPrice': web3.toWei('95', 'gwei'),
        'nonce': nonce,
    })

    # Sign & send the transaction that is the buying transaction
    
    signedTx = web3.eth.account.sign_transaction(uniSwap_tx, private_key = config.PRIVATE_KEY)
    tx_token = web3.eth.send_raw_transaction(signedTx.rawTransaction)
    # tx_status = web3.eth.get_transaction_receipt(tx_token)
    print('Transaction Ended Successfully with this Hash : ',web3.toHex(tx_token))
        
    # print(f' Your wallet address has : {readeable_token_balance} {token_symbol} after buying')


if __name__ == '__main__':
    BuyingProcess()

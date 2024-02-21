import time
from web3 import Web3
from etherscan import Etherscan

alchemy_url = "https://eth-goerli.alchemyapi.io/v2/API_KEY"

web3 = Web3(Web3.HTTPProvider(alchemy_url))

addr = "0x86fc885F3F7343ecFaB273f3fC0E91037a10A967"
private_key = "YOUR_PRIVATE_KEY"
DAI = "0x11fE4B6AE13d2a6055C8D9cF65c55bac32B5d844"
WETH = "0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6"
# uniswap_v3_router = web3.to_checksum_address("0xE592427A0AEce92De3Edee1F18E0157C05861564")
uniswap_v3_router = "0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45"

etherscan = Etherscan('S53YAY5FJ8QRTTPTR4IV36ZBN8UZX7TFJJ')

# load contracts
uniswap_v3_router_abi = etherscan.get_contract_abi(uniswap_v3_router)
WETH_ABI = etherscan.get_contract_abi(WETH)
# print(WETH_ABI)
DAI_ABI = etherscan.get_contract_abi(DAI)

contract = web3.eth.contract(address= uniswap_v3_router, abi= uniswap_v3_router_abi)
weth_contract = web3.eth.contract(address= WETH, abi= WETH_ABI)
# WETH9 = contract.functions.WETH9().call()
# # print(WETH9)

deadline = int(time.time()) + 1000 #17 minutes
# # print(start)

amount_in = 10000000000000000 # 0.01 * 10**18

token_approve = weth_contract.functions.deposit().build_transaction({
        'gas' : 300000,
        'maxPriorityFeePerGas': web3.eth.max_priority_fee,
        'maxFeePerGas': 100 * 10**9,
        'value': amount_in, # wrap 1 eth
        'nonce': web3.eth.get_transaction_count(addr),
    })

signed_approve_tx = web3.eth.account.sign_transaction(token_approve, private_key = private_key)
tx_token = web3.eth.send_raw_transaction(signed_approve_tx.rawTransaction)
print("Deposited hash : " + web3.to_hex(tx_token))

time.sleep(30)


# now approve the router to spend our weth
approve_tx = weth_contract.functions.approve(uniswap_v3_router, 2**256-1).build_transaction({
    'gas': 300000,  # Adjust the gas limit as needed
    "maxPriorityFeePerGas": web3.eth.max_priority_fee,
    "maxFeePerGas": 100 * 10**9,
    "nonce": web3.eth.get_transaction_count(addr),
}) 

raw_transaction = web3.eth.account.sign_transaction(approve_tx, private_key).rawTransaction
tx_hash = web3.eth.send_raw_transaction(raw_transaction)
# tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Approved hash : {Web3.to_hex(tx_hash)}")

time.sleep(5)

exact_input_params = (
    WETH, # tokenIn
    DAI, # tokenOut
    3000, # fee
    addr, # recipient
    #deadline, # deadline
    amount_in, # amount in
    0, # amountOutMinimum
    0 # sqrtPriceLimitX96
)

simple_swap = contract.functions.exactInputSingle(exact_input_params).build_transaction({
    "from" : addr,
    "maxPriorityFeePerGas": web3.eth.max_priority_fee,
    "maxFeePerGas": 110 * 10**9,
    "gas" : 300000,
    "nonce" : web3.eth.get_transaction_count(addr) + 1
})

signedTx = web3.eth.account.sign_transaction(simple_swap, private_key)
swapTx = web3.eth.send_raw_transaction(signedTx.rawTransaction)
# swap_receipt = web3.eth.wait_for_transaction_receipt(swapTx)
swapHash = web3.to_hex(swapTx)

print("Swap hash : " , swapHash)

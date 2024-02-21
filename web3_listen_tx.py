from web3 import Web3
import json
import asyncio
import signal
import time

alchemy_http = 'https://eth-rinkeby.alchemyapi.io/v2/API_KEY'
# alchemy_wss_testnet = 'wss://eth-rinkeby.alchemyapi.io/v2/API_KEY'

web3 = Web3(Web3.HTTPProvider(alchemy_http))

print(web3.isConnected())

opensea_eth_address = '0x7f268357A8c2552623316e2562D90e642bB538E5'

pancakeswap_router_address = '0x10ED43C718714eb63d5aA57B78B54704E256024E'
UNISWAP_V2 = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'
uniswap_v2 = '0x7a250d5630b4cf539739df2c5dacb4c659f2488d'
uniswap_router_address = '0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984'
UNISWAP_V3 = '0x24dc74E1540A48d873415d3d0973400A9f10DEDA'

tx_filter = web3.eth.filter('pending')
event_filter = tx_filter.get_new_entries()

def handler(signum, frame):
    res = input("Do you really want to stop the bot ? Y/n ")
    if res == 'y':
        exit(1)

signal.signal(signal.SIGINT, handler)

def handle_event(event):
    #get_tx = web3.eth.get_transaction_receipt(event)
    rs = Web3.toJSON(event)
    # rs_hex = Web3.toHex(event)
    res = rs.replace('"', '')
    
    try:
        result = web3.eth.get_transaction(res)
        receipt = web3.eth.get_transaction_receipt(res)
        # if(result):
        gas_price_wei = result['gasPrice']
        gas_price_eth = Web3.fromWei(gas_price_wei, 'ether')
        amount_eth = Web3.fromWei(result['value'], 'ether')
        
        print('\n====================  + TEMPORARILY PENDING TRANSACTION DETAILS + ====================')
        
        print('\nHash of a Pending Transaction:' , receipt)
        
            
    except:
        pass
        

async def log_loop(event_filter, interval):
    while True:
        for PendingTx in event_filter.get_new_entries():
            try:
                handle_event(PendingTx)
                await asyncio.sleep(interval)
            except:
                print('error ',handle_event(PendingTx))

def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(tx_filter, 2)))
    finally:
        loop.close()
    

if __name__ == "__main__":
    main()

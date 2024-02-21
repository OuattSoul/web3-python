from web3 import Web3
import json
import asyncio



url = 'INFURA_LINK'
# web3 = Web3(Web3.WebsocketProvider(moralis_wss_bsc))
web3 = Web3(Web3.HTTPProvider(url))

print(web3.isConnected())
# tx_hash = "0xac80bab0940f061e184b0dda380d994e6fc14ab5d0c6f689035631c81bfe220b"
# get_tx = web3.eth.get_transaction(tx_hash)

# print(get_tx)
opensea_eth_address = '0x7f268357A8c2552623316e2562D90e642bB538E5'

pancakeswap_router_address = '0x10ED43C718714eb63d5aA57B78B54704E256024E'
UNISWAP_V2 = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'
uniswap_v2 = '0x7a250d5630b4cf539739df2c5dacb4c659f2488d'
uniswap_router_address = '0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984'
UNISWAP_V3 = '0x24dc74E1540A48d873415d3d0973400A9f10DEDA'

tx_filter = web3.eth.filter('pending')
event_filter = tx_filter.get_new_entries()


def handle_event(event):
    #get_tx = web3.eth.get_transaction_receipt(event)
    rs = Web3.toJSON(event)
    # rs_hex = Web3.toHex(event)
    res = rs.replace('"', '')
    
    try:
        result = web3.eth.get_transaction(res)
        if(result):
            gas_price_wei = result['gasPrice']
            gas_price_eth = Web3.fromWei(gas_price_wei, 'ether')
            amount_eth = Web3.fromWei(result['value'], 'ether')
            
            if(amount_eth):

                # Truncate the data sent by the user by extracting only the 8 first digits in order to get the Method ID
                #input = result['input']
                #methodId = input[0:8]
                print('\n====================  + TEMPORARILY PENDING TRANSACTION DETAILS + ====================')
                print('\nHash of a Pending Transaction:' , result)
                print('\nTransaction Gas Price :' , gas_price_eth, ' ETH')
                print('\nTransaction Amount :' , amount_eth, ' ETH')
                print('\nAccount Nonce :' , result['nonce'])
                print('\nSent To :' , result['to'])
    except:
        print('\n+=======================================  + ONLY LONG PENDING TRANSACTION HASHES + =========================================+')
        print('\n"Transaction hash : ', web3.toHex(event))
        print('\n+=======================================  + END + =========================================+')
        
        # print("Waiting...")
    

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

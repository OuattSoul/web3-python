
from web3 import Web3


main_alchemy_http = 'https://eth-mainnet.g.alchemy.com/v2/API_KEy'
web3 = Web3(Web3.HTTPProvider(main_alchemy_http)) 


UNISWAPV2FACTORY = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
SUSHISWAPV2FACTORY = "0xC0AEe478e3658e2610c5F7A4A2E1777cE9e4f2Ac"
STEPNFACTORY = "0x1e895bFe59E3A5103e8B7dA3897d1F2391476f3c"
SHIBASWAPFACTORY = "0x115934131916C8b277DD010Ee02de363c09d037c"
ONEINCHFACTORY= "0xbAF9A5d4b0052359326A6CDAb54BABAa3a3A9643"

UNISWAPV2FACTORYABI = '[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
factory_contract = web3.eth.contract(address = SUSHISWAPV2FACTORY, abi = UNISWAPV2FACTORYABI) # when address et abi parameters are not specify, we must add the third parameter that is provider 
exchange_abi = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

token1 = web3.toChecksumAddress('0x6b175474e89094c44da98b954eedeac495271d0f') # 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48
token2 = web3.toChecksumAddress('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2') # 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2

price_list = {}


class TokenPrices():

    # def GetPrice():
    #     print()


    def GetPriceOnUNISWAP(self,token_address):
        market = "UNISWAP"
        factory_contract = web3.eth.contract(address = token_address, abi = UNISWAPV2FACTORYABI) # when address et abi parameters are not specify, we must add the third parameter that is provider 

        get_pair = factory_contract.functions.getPair(token2,token1).call()

        token1_contract = web3.eth.contract(address = token1, abi = exchange_abi)
        token1_symbol = token1_contract.functions.symbol().call()
        token1_decimals = token1_contract.functions.decimals().call()

        token2_contract = web3.eth.contract(address = token2, abi = exchange_abi)
        token2_symbol = token2_contract.functions.symbol().call()
        token2_decimals = token2_contract.functions.decimals().call()

        print('\n=====================Pair contract address UNISWAP : ',get_pair)

        # get reserves in uniswap
        print('\n -----------------------Get Token Reserves on UNISWAP-----------------------\n')
        print("\nToken 1 =====> Address : ", token1, " Symbol : ", token1_symbol)
        # print("\nToken 1 decimals : ", token1_decimals)

        print("\nToken 2 =====> Address : ", token2, " Symbol : ", token2_symbol)
        # print("\nToken 2 decimals : ", token2_decimals)

        exchange_contract = web3.eth.contract(address= get_pair, abi = exchange_abi)
        get_reserves = exchange_contract.functions.getReserves().call()
        # print(get_reserves)

        # get token prices
        print('token 1 price : ',get_reserves[0])
        print('token 2 price : ',get_reserves[1])
        # print('price is : ', get_reserves[1] / get_reserves[0])

        price = get_reserves[1] / get_reserves[0]
        
        price1 = get_reserves[0] / get_reserves[1]
        print('price is : ', price)
        ajusted_price = price / (10 ** (token2_decimals - token1_decimals))
        print("price1 ",price1)
        inverted_price = 1 / ajusted_price
        # print('token price : ',inverted_price)
        price_list.update({market:inverted_price})
        print(f'1 {token2_symbol} ===> {inverted_price} {token1_symbol}')
        print('\n************************END************************')


    def GetPriceOnSUSHISWAP(self,token_address):
        market = "SUSHISWAP"
        factory_contract = web3.eth.contract(address = token_address, abi = UNISWAPV2FACTORYABI) # when address et abi parameters are not specify, we must add the third parameter that is provider 

        get_pair = factory_contract.functions.getPair(token2,token1).call()

        token1_contract = web3.eth.contract(address = token1, abi = exchange_abi)
        token1_symbol = token1_contract.functions.symbol().call()
        token1_decimals = token1_contract.functions.decimals().call()

        token2_contract = web3.eth.contract(address = token2, abi = exchange_abi)
        token2_symbol = token2_contract.functions.symbol().call()
        token2_decimals = token2_contract.functions.decimals().call()

        print('\n=====================Pair contract address SUSHISWAP : ',get_pair)

        # get reserves in uniswap
        print('\n -----------------------Get Token Reserves on SUSHISWAP-----------------------\n')
        print("\nToken 1 =====> Address : ", token1, " Symbol : ", token1_symbol)
        # print("\nToken 1 decimals : ", token1_decimals)

        print("\nToken 2 =====> Address : ", token2, " Symbol : ", token2_symbol)
        # print("\nToken 2 decimals : ", token2_decimals)

        exchange_contract = web3.eth.contract(address= get_pair, abi = exchange_abi)
        get_reserves = exchange_contract.functions.getReserves().call()
        # print(get_reserves)

        # get token prices
        print('token 1 price : ',get_reserves[0])
        print('token 2 price : ',get_reserves[1])
        # print('price is : ', get_reserves[1] / get_reserves[0])

        price = get_reserves[1] / get_reserves[0]
        print('price is : ', price)
        ajusted_price = price / (10 ** (token2_decimals - token1_decimals))
        # print(ajusted_price)
        inverted_price = 1 / ajusted_price
        # print('token price : ',inverted_price)
        price_list.update({market:inverted_price})
        print(f'1 {token2_symbol} ===> {inverted_price} {token1_symbol}')
        print('\n************************END************************')


    def GetPriceOnSHIBASWAP(self,token_address):
        market = "SHIBASWAP"
        factory_contract = web3.eth.contract(address = token_address, abi = UNISWAPV2FACTORYABI) # when address et abi parameters are not specify, we must add the third parameter that is provider 

        get_pair = factory_contract.functions.getPair(token2,token1).call()

        token1_contract = web3.eth.contract(address = token1, abi = exchange_abi)
        token1_symbol = token1_contract.functions.symbol().call()
        token1_decimals = token1_contract.functions.decimals().call()

        token2_contract = web3.eth.contract(address = token2, abi = exchange_abi)
        token2_symbol = token2_contract.functions.symbol().call()
        token2_decimals = token2_contract.functions.decimals().call()

        print('\n=====================Pair contract address SHIBASWAP : ',get_pair)

        # get reserves in uniswap
        print('\n -----------------------Get Token Reserves on SHIBASWAP-----------------------\n')
        print("\nToken 1 =====> Address : ", token1, " Symbol : ", token1_symbol)
        # print("\nToken 1 decimals : ", token1_decimals)

        print("\nToken 2 =====> Address : ", token2, " Symbol : ", token2_symbol)
        # print("\nToken 2 decimals : ", token2_decimals)

        exchange_contract = web3.eth.contract(address= get_pair, abi = exchange_abi)
        get_reserves = exchange_contract.functions.getReserves().call()
        # print(get_reserves)

        # get token prices
        print('token 1 price : ',get_reserves[0])
        print('token 2 price : ',get_reserves[1])
        # print('price is : ', get_reserves[1] / get_reserves[0])

        price = get_reserves[1] / get_reserves[0]
        print('price is : ', price)
        ajusted_price = price / (10 ** (token2_decimals - token1_decimals))
        # print(ajusted_price)
        inverted_price = 1 / ajusted_price
        # print('token price : ',inverted_price)
        price_list.update({market:inverted_price})
        print(f'1 {token2_symbol} ===> {inverted_price} {token1_symbol}')
        print('\n************************END************************')


    def GetPriceOnSTEPN(self,token_address):
        market = "STEPN"
        factory_contract = web3.eth.contract(address = token_address, abi = UNISWAPV2FACTORYABI) # when address et abi parameters are not specify, we must add the third parameter that is provider 

        get_pair = factory_contract.functions.getPair(token2,token1).call()

        token1_contract = web3.eth.contract(address = token1, abi = exchange_abi)
        token1_symbol = token1_contract.functions.symbol().call()
        token1_decimals = token1_contract.functions.decimals().call()

        token2_contract = web3.eth.contract(address = token2, abi = exchange_abi)
        token2_symbol = token2_contract.functions.symbol().call()
        token2_decimals = token2_contract.functions.decimals().call()

        print('\n=====================Pair contract address STEPN : ',get_pair)

        # get reserves in uniswap
        print('\n -----------------------Get Token Reserves on STEPN-----------------------\n')
        print("\nToken 1 =====> Address : ", token1, " Symbol : ", token1_symbol)
        # print("\nToken 1 decimals : ", token1_decimals)

        print("\nToken 2 =====> Address : ", token2, " Symbol : ", token2_symbol)
        # print("\nToken 2 decimals : ", token2_decimals)

        exchange_contract = web3.eth.contract(address= get_pair, abi = exchange_abi)
        get_reserves = exchange_contract.functions.getReserves().call()
        # print(get_reserves)

        # get token prices
        print('token 1 price : ',get_reserves[0])
        print('token 2 price : ',get_reserves[1])
        # print('price is : ', get_reserves[1] / get_reserves[0])

        price = get_reserves[1] / get_reserves[0]
        print('price is : ', price)
        ajusted_price = price / (10 ** (token2_decimals - token1_decimals))
        # print(ajusted_price)
        inverted_price = 1 / ajusted_price
        # print('token price : ',inverted_price)
        price_list.update({market:inverted_price})
        print(f'1 {token2_symbol} ===> {inverted_price} {token1_symbol}')
        print('\n************************END************************')





    def main(self):
        p.GetPriceOnUNISWAP(UNISWAPV2FACTORY)
        p.GetPriceOnSUSHISWAP(SUSHISWAPV2FACTORY)
        p.GetPriceOnSHIBASWAP(SHIBASWAPFACTORY)
        p.GetPriceOnSTEPN(STEPNFACTORY)
        print('\n\n Price by Markets',price_list)

       

        for name,price in price_list.items():
            
            
            print(f'Market : {name} Price : {price}')
            min_key = min(price_list, key=price_list.get)
            max_key = max(price_list, key=price_list.get)

            min_val = min(price_list.values())
            max_val = max(price_list.values())
        
        print(f'\nMinimum Price is : {min_val} & Maximum Price is :{max_val}')
        print(f'\nBuy On {min_key} & Sell on {max_key}')

        price_key = list(price_list.keys())
        price_value = list(price_list.values())
        print(price_value[0],price_value[1],price_value[2],price_value[3])


p = TokenPrices()
p.main()


# if __name__ == '__main__':

#     main()

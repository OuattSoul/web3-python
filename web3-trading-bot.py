import math
from numpy import append
from web3 import Web3
import time
import uniSwapABI
import config

def Interface():

    import os


    # sets the text colour to green 
    os.system("tput setaf 2")
    
    print("Launching Terminal User Interface...\n")
    

    # sets the text color to red
    os.system("tput setaf 1")

    print("\t\tWelcome To Smart Trading Terminal User Interface\t\t\t")
    
    # sets the text color to white
    os.system("tput setaf 4")
    
    print("\t-------------------------------------------------")
    # print("Enter a number to do an action")

    while True:
        print("""
            \tEnter a number to do an action \t
            1 - Begin Trading
            2 - Display all my Tokens and their Balances
            3 - Add a new Token
            4 - Enter the Tokens you want to trade 
            0 - Exit""")
    
        ch=int(input("\nEnter your choice: "))
    
        if(ch == 1):
            main()
    
        elif ch == 2:
            
            DisplayAllTokens()
            print("\n")
    
        elif ch == 3:
            AddTokenToList()

        else:
            print("Invalid entry")
    
        input("Press enter to continue or CTRL + C to exit ")
        os.system("clear")

alchemy_http = 'https://eth-rinkeby.alchemyapi.io/v2/API_KEY'
web3 = Web3(Web3.HTTPProvider(alchemy_http))

wallet_address = "0xe3242ca2b4036f90f42C6D7861af28d06c6161cC"

# value = input("\nWhat is the amount of ETH you want to expend :")

# gas_price = input("\nEnter the amount of gasPrice you are willing to pay :")

uniRouterContractAddress = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D' # uniswap contract address on testnet 

contract  = web3.eth.contract(address = uniRouterContractAddress, abi = uniSwapABI.uniABI)

wrapped_address = web3.toChecksumAddress("0xc778417e063141139fce010982780140aa0cd5ab") # weth address on testnet 0xc778417E063141139Fce010982780140Aa0cD5Ab


start = time.time()

amountIn = 0

def AddTokenToList():
    new_token = input("\nEnter a new Token Address :")
    new_token_array = DisplayAllTokens.tokens_array
    new_token_array.append(new_token)
    print("\n",new_token_array)


def DisplayAllTokens():
    link = "0x01BE23585060835E02B77ef475b0Cc51aA1e0709"
    dai = "0x5592EC0cfb4dbc12D3aB100b257153436a1f0FEa"
    dAITokenMock = "0xaD6Db97C844Ec7Bb4c0641d436AA0D395fDD3f45"
    uni = "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984"
    mToken = "0x6BD8d4c37ADB8fe976c19506012896012Da63B40"
    testUSDC = "0xA6Cc591f2Fd8784DD789De34Ae7307d223Ca3dDc"
    two = "0xE73bcbaF9ff36D66C5b7805c8c64D389FD7fdb75"
    blueJay = "0x787f7893474191847c7DDF3a9040509f225Dd820"
    lusdc = "0x787f7893474191847c7DDF3a9040509f225Dd820"
    mockedDAI = "0x34270631F44C24fc320283347c38515798fA4388"
    tokenUSDT = "0x045144F7532E498694d7Aae2d88E176c42c0ff97"
    govOfficialTest = "0xf945e543b997ef54d8dFC20e89F3A8465Fe5Ee9d"


    DisplayAllTokens.tokens_array = [link,dai,dAITokenMock,uni,mToken,testUSDC,two,blueJay,lusdc,mockedDAI,tokenUSDT]
    
    print("\n",DisplayAllTokens.tokens_array)

def TokensToTrade():
    tokens_to_trade_array = []


def SwapExactEthForTokens():
    nonce = web3.eth.getTransactionCount(wallet_address)

    value = input("\nWhat is the amount of ETH you want to expend :")

    amountOutMin = handle_event.amountOut
    print('Amount out :', amountOutMin)
    tokenToBuy = handle_event.tokenToBuy
    print('Token to buy : ', tokenToBuy)

    uniSwap_tx = contract.functions.swapExactETHForTokens(

        amountOutMin,
        [wrapped_address, tokenToBuy],
        wallet_address,
        (int(time.time()) + 10000)
    ).buildTransaction({
        'from': wallet_address,
        'value': web3.toWei(value, 'ether'),
        'gas': 300000,
        'gasPrice': web3.toWei('15', 'gwei'),
        'nonce': web3.eth.getTransactionCount(wallet_address),
    })

    # Sign & send the transaction that is the buying transaction
    signedTx = web3.eth.account.sign_transaction(uniSwap_tx, private_key = config.PRIVATE_KEY)
    tx_token = web3.eth.send_raw_transaction(signedTx.rawTransaction)
    print('Transaction Hash : ',web3.toHex(tx_token))

    time.sleep(20)
    try:
        SellingProcess()
    except Exception as e:
        print(e)

def SellingProcess():

    # ourGasPrice = handle_event.ourGasPrice
    balance = web3.eth.getBalance(wallet_address)
    readeable_balance = web3.fromWei(balance, 'ether')
    print('\nActual Balance before selling your token is : ',readeable_balance, "ETH")

    tokenToSell = handle_event.tokenToBuy
    print('Token to sell back :', tokenToSell)
    contract  = web3.eth.contract(address = uniRouterContractAddress, abi = uniSwapABI.uniABI)

    sellABI = '[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint8","name":"_decimals","type":"uint8"},{"internalType":"uint256","name":"supply","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"wrapped_addresser","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"wrapped_addresser","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"wrapped_addresser","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"wrapped_addresser","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"wrapped_addresser","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'

    sellTokenContract = web3.eth.contract(tokenToSell, abi = sellABI)

    tokenBalance = sellTokenContract.functions.balanceOf(wallet_address).call()
    tokenSymbol = sellTokenContract.functions.symbol().call()
    readeable_token_balance = web3.fromWei(tokenBalance, 'ether')
    print("Your Token " + tokenSymbol + " Balance is : " + str(readeable_token_balance) + ' ' + tokenSymbol)

    sell_token_value = Web3.toWei(math.trunc(readeable_token_balance), 'ether')
    sell_token_value_ether = web3.fromWei(sell_token_value, 'ether')
    print("You are going to sell this amount of your Token",sell_token_value_ether, " ", tokenSymbol)  

    try:
        token_approve = sellTokenContract.functions.approve(uniRouterContractAddress, tokenBalance).buildTransaction({
            'from': wallet_address,
            'gas': 300000,
            'gasPrice': web3.toWei('15', 'gwei'),
            # 'nonce': nonce_nb,
            'nonce': web3.eth.getTransactionCount(wallet_address),
        })

        signedTx = web3.eth.account.sign_transaction(token_approve, private_key = config.PRIVATE_KEY)
        tx_token = web3.eth.send_raw_transaction(signedTx.rawTransaction)
        print("Approved Transaction Hash is : " + web3.toHex(tx_token))
    except Exception as e:
        print("Approval failed ", e)

    #after approve, wait for 10 sec before sending the tx
    time.sleep(10)  

    print(f"Swapping {sell_token_value_ether} {tokenSymbol} for ETH") 

    try:
        uniSwap_tx = contract.functions.swapExactTokensForETH(
            sell_token_value,
            0,
            [tokenToSell, wrapped_address],
            wallet_address,
            (int(time.time()) + 1000000)
        ).buildTransaction({
            'from': wallet_address,
            'gas': 300000,
            'gasPrice': web3.toWei(20, 'gwei'),
            # 'gasPrice': web3.toWei('20', 'gwei'),
            # 'nonce': nonce3,
            'nonce': (web3.eth.getTransactionCount(wallet_address)+1),
        })

        signedTxn = web3.eth.account.sign_transaction(uniSwap_tx, private_key = config.PRIVATE_KEY)
        txn_token = web3.eth.send_raw_transaction(signedTxn.rawTransaction)
        print(f"Sold {tokenSymbol} " + web3.toHex(txn_token))
    except Exception as e:
        print("Selling failed ", e)

    time.sleep(10)



def handle_event(event):
    rs = Web3.toJSON(event)
    res = rs.replace('"', '')
    try:
        result = web3.eth.get_transaction(res)
        res_input = result['input']
        methodId = res_input[0:10]
        print('\nGot results')
        # print('\nMethod ID : ',methodId)
        
        # if(methodId == '0x38ed1739' or methodId == '0x8803dbee' or methodId == '0x7ff36ab5' or methodId == '0xfb3bdb41'):
        if(methodId == '0x38ed1739'):

            print("\n==================================== Swap Exact Tokens For Tokens ====================================")
            print('\n',result)

            amountOut = res_input[74:138]
            # print('\nAmount Ou Min HEX : ',amountOut)
            amountOutDEC = int(amountOut, 16)

            print('\nTarget 1 Amount Out Min DEC : ',amountOutDEC)
            print('Amount Being Trading : ',amountOutDEC * 10**-18)
            amountToBuy = amountOutDEC * 10**-18
            handle_event.amountOut = math.trunc(amountToBuy)
            
            print('\nAmount Out : ',handle_event.amountOut)

            target = res_input[458:522]
            print(target)
            # target2 = '0x'+target2[24:64]
            print('\nTarget 2 Address : ','0x'+target[24:64])
            target2 = '0x'+target[24:64]

            handle_event.tokenToBuy = web3.toChecksumAddress(target2)
            
            print('\nMethod ID : ',methodId)

            # Buying Process
            # try:
            #     BuyingProcess()
            # except Exception as e:
            #     print('Error in Buying process : ', e)
                    
    

        elif(methodId == '0x8803dbee'):
            
            print("\n==================================== Swap Tokens For Exact Tokens ====================================")
            print('\n',result)

            amountOut = res_input[10:74]
            # print('\nAmount Ou Min HEX : ',amountOut)
            amountOutDEC = int(amountOut, 16)

            print('\nTarget 1 Amount Ou Min DEC : ',amountOutDEC)
            print(amountOutDEC * 10**-18)

            target = res_input[458:522]
            print(target)
            # target2 = '0x'+target2[24:64]
            print('\nTarget 2 Address : ','0x'+target[24:64])

        elif(methodId == '0x7ff36ab5'):
            
            print("\n==================================== Swap Exact ETH For Tokens ====================================")
            print('\n',result)

            amountOut = res_input[10:74]
            # print('\nAmount Ou Min HEX : ',amountOut)
            amountOutDEC = int(amountOut, 16)

            print('\nTarget 1 Amount Ou Min DEC : ',amountOutDEC)
            print('Amount Being Trading : ',amountOutDEC * 10**-18)
            amountToBuy = amountOutDEC * 10**-18
            handle_event.amountOut = math.trunc(amountToBuy)
            print('\nAmount Out : ',handle_event.amountOut)

            target = res_input[394:458]
            print(target)
            # target2 = '0x'+target2[24:64]
            print('\nTarget 2 Address : ', '0x'+target[24:64])

            target2 = '0x'+target[24:64]

            handle_event.tokenToBuy = web3.toChecksumAddress(target2)
            
            print('\nMethod ID : ',methodId)

            # Buying Process
            try:
                SwapExactEthForTokens()
            except Exception as e:
                print('Error in Buying process : ', e)

            

        elif(methodId == '0xfb3bdb41'):
            
            print("\n==================================== Swap ETH For Exact Tokens ====================================")
            print('\n',result)

            amountOut = res_input[10:74]
            # print('\nAmount Ou Min HEX : ',amountOut)
            amountOutDEC = int(amountOut, 16)

            print('\nTarget 1 Amount Ou Min DEC : ',amountOutDEC)
            print(amountOutDEC * 10**-18)

            amountToBuy = amountOutDEC * 10**-18
            handle_event.amountOut = math.trunc(amountToBuy)
            print('\nAmount Out : ',handle_event.amountOut)

            target = res_input[394:458]
            print(target)
            # target2 = '0x'+target2[24:64]
            print('\nTarget 2 Address : ', '0x'+target[24:64])

            target2 = '0x'+target[24:64]

            handle_event.tokenToBuy = web3.toChecksumAddress(target2)
            
            print('\nMethod ID : ',methodId)
       
    except:
        pass

def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)


    

def main():
    block_filter = web3.eth.filter('pending')
    log_loop(block_filter, 2)

if __name__ == '__main__':
    Interface()

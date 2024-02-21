from web3 import Web3


# Our end points
url = "https://eth-rinkeby.alchemyapi.io/v2/API_KEY"
# url = "https://eth-mainnet.g.alchemy.com/v2/API_KEY"
ws_url = "wss://eth-mainnet.alchemyapi.io/v2/API_KEY"

# Connect to the blockchain through web3
web3 = Web3(Web3.HTTPProvider(mainnet))

# Set up the starting block number
startBlock = web3.eth.blockNumber - 17280 # 17280 is approximatively the number of blocks created by day

# Set up the end block number
endBlock = web3.eth.blockNumber

# We filter the blockchain by getting the data from a block number to another
filter_tx = web3.eth.filter({"fromBlock": startBlock, "toBlock": endBlock})

# Get all the entries in realtime
response = filter_tx.get_all_entries()

# Make a loop to go through all the entries got 
for entry in response:
    
    # Get the transaction hash from the entries
    rs = Web3.toJSON(entry['transactionHash'])

    # Decode to a readeable format
    res = rs.replace('"', '')

    # Get the data from the new readeable transaction hash 
    data = web3.eth.get_transaction(res)

    # Retrieve the input field
    input = data["input"]

    # From the input field, extract the Method Id that is the 10 first digits
    methodID = input[0:10]

    # Try to get the below variables...
    try:
        # retrieve the block number from transaction
        blockNumber = data['blockNumber']

        # retrieve the gas price from transaction
        gasPrice = data['gasPrice']

        # retrieve the max fee per gas from transaction
        maxFeePerGas = data['maxFeePerGas']

        # retrieve the max priority fee per gas from transaction
        maxPriorityFeePerGas = data['maxPriorityFeePerGas']

        # MethodID dictionary
        # swapout 0x628d6cba
        # swap 0x7c025200
        # uniswapV3Swap 0xe449022e
        # swapETHForExactTokens 0x7419c508
        # multicall 0x5ae401dc
        # sellToUniswap 0xd9627aa4
        # unoswap 0x2e95b6c8
        # swap 0x67641c2f
        # execute 0x1cff79cd
        # swap 0x7c025200
        methodIDList = ["0x38ed1739","0x8803dbee","0x7ff36ab5","0xfb3bdb41","0x628d6cba","0x7c025200","0xe449022e","0x7419c508","0x5ae401dc","0xd9627aa4","0x2e95b6c8","0x67641c2f"]
        
        # Check whether the method id got corresponds to our method id list
        if(methodID in methodIDList ):

            # Print the data found
            print("\nTransaction Hash : ",res,
                "\nBlock Number : ",blockNumber,
                "\nGas Price : ",gasPrice,
                "\nMax Fee Per Gas : ",maxFeePerGas,
                "\nMax Priority Fee Per Gas : ",maxPriorityFeePerGas
            )
    # Otherwise raise an exception withe the error found
    except Exception as e:
        pass
        # print('\nData not found ',e)

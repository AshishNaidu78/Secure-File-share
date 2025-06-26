from web3 import Web3
import json, os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path='../ganache/.env')

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider(os.getenv("RPC_URL")))

# Load ABI
with open("blockchain/FileRegistryABI.json") as f:
    abi = json.load(f)

# Load Contract
contract = w3.eth.contract(address=os.getenv("CONTRACT_ADDRESS"), abi=abi)

# Register File Function
def register_file(file_id, file_hash):
    acct = w3.eth.account.from_key(os.getenv("PRIVATE_KEY"))
    nonce = w3.eth.get_transaction_count(acct.address)

    tx = contract.functions.registerFile(file_id, file_hash).build_transaction({
        'from': acct.address,
        'nonce': nonce,
        'gas': 300000,
        'gasPrice': w3.to_wei('5', 'gwei')
    })

    signed_tx = w3.eth.account.sign_transaction(tx, acct.key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    return tx_hash.hex()

def get_file_metadata(file_id):
    result = contract.functions.getFile(file_id).call()
    return result[0], result[1], result[2]  # hash, uploader, timestamp
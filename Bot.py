from web3 import Web3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to Polygon network
infura_url = os.getenv("INFURA_URL")
web3 = Web3(Web3.HTTPProvider(infura_url))

print("Connected to Polygon:", web3.isConnected())

# Wallet info
wallet_address = os.getenv("WALLET_ADDRESS")
private_key = os.getenv("PRIVATE_KEY")

# Token pair addresses
token_address = os.getenv("TOKEN_ADDRESS")
pair_address = os.getenv("PAIR_ADDRESS")

# Check balance
def check_balance():
    balance = web3.eth.get_balance(wallet_address)
    print("Wallet balance:", web3.fromWei(balance, 'ether'), "MATIC")

check_balance()

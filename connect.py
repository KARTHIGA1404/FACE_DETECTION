import pandas as pd
from pymongo import MongoClient
from web3 import Web3
import hashlib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Web3
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Get environment variables
user_private_key = os.getenv('ETH_PRIVATE_KEY')
if user_private_key and not user_private_key.startswith('0x'):
    user_private_key = '0x' + user_private_key

user_address = os.getenv('ETH_ADDRESS')
if user_address:
    user_address = web3.to_checksum_address(user_address)

# Step 1: Load dataset
def load_csv(file_path):
    data = pd.read_csv(file_path)
    return data

# Step 2: Connect to MongoDB and insert data
def insert_to_mongodb(data, db_name, collection_name):
    client = MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db[collection_name]
    data_dict = data.to_dict(orient='records')
    collection.insert_many(data_dict)
    return collection

# Step 3: Generate hash for the dataset
def generate_hash(data):
    data_string = data.to_csv(index=False)
    return hashlib.sha256(data_string.encode()).hexdigest()

# Step 4: Store hash on blockchain
def store_hash_on_blockchain(web3, contract_address, contract_abi, dataset_hash, private_key):
    try:
        contract = web3.eth.contract(address=contract_address, abi=contract_abi)
        store_hash_func = contract.get_function_by_name('storeHash')
        
        transaction = {
            'from': user_address,
            'gas': 2000000,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(user_address),
            'to': contract_address,
            'data': store_hash_func(dataset_hash).build_transaction()['data']
        }
        
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
        web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    except Exception as e:
        pass

if __name__ == "_main_":
    try:
        # Provide the path to your dataset
        file_path = "person.csv"
        
        # Step 1: Load dataset
        data = load_csv(file_path)

        # Step 2: Insert into MongoDB
        db_name = "KaggleDB"
        collection_name = "Dataset"
        insert_to_mongodb(data, db_name, collection_name)

        # Step 3: Generate hash
        dataset_hash = generate_hash(data)

        # Step 4: Connect to blockchain and store hash
        contract_address = web3.to_checksum_address("0xd8b934580fcE35a11B58C6D73aDeE468a2833fa8")
        contract_abi = [
            {
                "inputs": [
                    {
                        "internalType": "string",
                        "name": "_hash",
                        "type": "string"
                    }
                ],
                "name": "storeHash",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "inputs": [],
                "name": "getHash",
                "outputs": [
                    {
                        "internalType": "string",
                        "name": "",
                        "type": "string"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            }
        ]

        store_hash_on_blockchain(web3, contract_address, contract_abi, dataset_hash, user_private_key)

    except Exception:
        pass
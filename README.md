
**Project Overview**
This project demonstrates a system to securely store a hash of a dataset on the Ethereum blockchain. The system involves:
1. Loading a dataset from a CSV file.
2. Storing the dataset in a MongoDB database.
3. Generating a SHA-256 hash of the dataset.
4. Storing the hash on the Ethereum blockchain using a smart contract.

**Technologies Used**
- **Python**: Programming language for building the system.
- **Pandas**: For loading and processing the dataset.
- **MongoDB**: To store the dataset.
- **Web3.py**: To interact with the Ethereum blockchain.
- **Hashlib**: For generating the SHA-256 hash.
- **Dotenv**: To manage environment variables.
- **Ethereum Blockchain**: To securely store the dataset hash.

**Prerequisites**
Ensure you have the following installed:
1. Python 3.7 or above
2. MongoDB
3. Node.js (for setting up an Ethereum testnet like Ganache)
4. Ethereum client (e.g., Ganache or Infura)

**Installation Steps**

1. Clone the Repository
```bash
# Clone this repository to your local machine
git clone <repository_url>
cd <repository_folder>
```

2. Install Python Dependencies
```bash
# Install required Python libraries
pip install pandas pymongo web3 python-dotenv
```

3. Set Up Environment Variables
Create a `.env` file in the project root directory and add the following:
```
ETH_PRIVATE_KEY=<Your Ethereum Private Key>
ETH_ADDRESS=<Your Ethereum Wallet Address>
```

4. Set Up MongoDB
1. Install MongoDB ([Download here](https://www.mongodb.com/try/download/community)).
2. Start the MongoDB service:
   ```bash
   mongod
   ```

5. Set Up Ethereum Blockchain
1. Install and launch Ganache or use Infura for a live testnet.
2. Deploy the provided smart contract to your Ethereum blockchain:
   ```solidity
   pragma solidity ^0.8.0;

   contract HashStorage {
       string private storedHash;

       function storeHash(string memory _hash) public {
           storedHash = _hash;
       }

       function getHash() public view returns (string memory) {
           return storedHash;
       }
   }
   ```

3. Note the deployed contract address and replace it in the script.

6. Run the Script
1. Place your dataset CSV file in the project directory and update the `file_path` variable in the script.
2. Run the script:
   ```bash
   python script.py
   ```

**How It Works**
1. **Load Dataset**: The script reads a dataset from the specified CSV file using Pandas.
2. **Insert into MongoDB**: The dataset is inserted into MongoDB as a collection.
3. **Generate Hash**: A SHA-256 hash is computed for the dataset.
4. **Store Hash on Blockchain**: The hash is stored on the Ethereum blockchain using a smart contract.

**Additional Notes**
- Make sure the Ethereum client is running and accessible at `http://127.0.0.1:8545`.
- Replace placeholders like `<repository_url>` and `<Your Ethereum Private Key>` with actual values.

**License**
This project is licensed under the MIT License. See the LICENSE file for details.


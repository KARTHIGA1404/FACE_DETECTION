#**CODE IS KUMARAGURU COLLEGE OF TECHNOLOGY'S ASSESTS**#

**PROJECT DESCRIPTION**

Suspect Detection & Blockchain Integration Project
This project integrates Flask with real-time face recognition and alerts, with blockchain-based data verification and storage. It uses Flask-SocketIO to send real-time status updates and MongoDB to store and manage data. It also integrates with Web3 to store dataset hashes on the Ethereum blockchain for security and integrity.

**Features**

- **Real-time Face Recognition**: Detect faces in videos and compare them with known faces.
- **Alert System**: Notify a website interface when a face is detected and matched.
- **MongoDB Integration**: Store data such as face recognition details in a MongoDB database.
- **Blockchain Verification**: Hash dataset and store the hash on the Ethereum blockchain for integrity verification.

**Requirements**

1. Python 3.x
2. MongoDB
3. Web3.py (Ethereum blockchain interaction)
4. OpenCV for video processing
5. Flask & Flask-SocketIO for web application and real-time communication
6. Face Recognition library for face detection

**Installation Steps**

1. Clone the repository

```bash
git clone https://github.com/your-repository.git
cd your-repository
```

2. Install dependencies

Create a virtual environment and install required libraries:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

The `requirements.txt` file should contain:

```
Flask==2.2.3
Flask-SocketIO==5.3.0
opencv-python==4.7.0.72
face_recognition==1.3.0
pymongo==4.3.3
web3==6.1.0
pandas==1.5.3
python-dotenv==1.0.0
```

3. Set up MongoDB

Ensure MongoDB is running on your machine or use a remote MongoDB service. You can install MongoDB from [here](https://www.mongodb.com/try/download/community).

4. Configure Environment Variables

Create a `.env` file in the root of the project and add your Ethereum private key and address:

```plaintext
ETH_PRIVATE_KEY=your_private_key
ETH_ADDRESS=your_wallet_address
```

5. Run the Flask Application

Start the Flask application by running:

```bash
python app.py
```

This will start the Flask server at `http://127.0.0.1:5000/`.

6. Run the Face Recognition Script

To run the face recognition script, execute the following command:

```bash
python face_recognition_script.py
```

This script will process the video file `v7.mp4`, compare faces with `person4.jpg` and `person5.jpg`, and send alerts to the Flask application if a match is found.

7. Blockchain Integration

The script will also generate a hash of the dataset from `person.csv` and store it on the Ethereum blockchain for verification. Ensure you have access to an Ethereum node or use a local Ethereum instance running at `http://127.0.0.1:8545`.

Project Structure

```bash
.
├── app.py                        # Flask app
├── face_recognition_script.py    # Script to handle face recognition and alert system
├── person.csv                    # Dataset containing person data
├── person4.jpg                   # Image for face comparison
├── person5.jpg                   # Image for face comparison
├── v7.mp4                        # Video for face detection
├── .env                          # Environment variables for Ethereum private key and address
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

How It Works

1. **Face Recognition**:
   - The face recognition script loads a video file (`v7.mp4`), processes it frame by frame, and compares faces with known images (`person4.jpg`, `person5.jpg`).
   - If a match is found, an alert with the person's information is sent to the Flask app.

2. **Flask App**:
   - The Flask app listens for updates from the face recognition script via Flask-SocketIO.
   - When a match is detected, the app emits an alert with the status and person's information.

3. **Blockchain Integration**:
   - The dataset (`person.csv`) is loaded and hashed.
   - The hash is then stored on the Ethereum blockchain to ensure data integrity and verifiability.

**Blockchain Setup**

Ensure your Ethereum private key and address are correctly configured in the `.env` file. The smart contract method `storeHash` is used to store the dataset hash on the blockchain. You'll need to deploy the contract at the specified `contract_address`.

**License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**FOR STORING DATA IN BLOCKCHAIN**

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
   python connect.py
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


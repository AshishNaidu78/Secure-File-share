# 🔐 Blockchain-Based Secure File Sharing System with **hybrid cryptography (AES + RSA)** and **Ethereum blockchain**

A full-stack secure file sharing system that enables encrypted file upload and download using **hybrid cryptography (AES + RSA)**, digital signatures for authenticity, and **Ethereum blockchain** for immutable file metadata verification.

---

## 🧩 Key Components

### 1. 🔐 Hybrid Cryptography
- **AES (Advanced Encryption Standard)**: Encrypts the actual file (symmetric encryption).
- **RSA**: Encrypts the AES key with the receiver’s public key (asymmetric encryption).
- **Digital Signatures (RSA-PSS)**: Ensures file authenticity and non-repudiation.

### 2. 🛠 Flask Backend
Handles:
- File upload and encryption
- Signature generation and verification
- Metadata storage on blockchain (Web3.py)
- File download and decryption
- Blockchain-based integrity verification

### 3. ⚛ React Frontend
- Upload form with user input
- Download form with file decryption metadata
- File verification form

### 4. ⛓️ Blockchain Integration (via Remix + Ganache)
- Smart contract written in Solidity (`SmartContract.sol`)
- Deployed using **Remix** and **MetaMask** to **Ganache local blockchain**
- Stores: file hash, file ID, uploader address, timestamp

---

## 📁 Project Structure

```
secure-file-share/
├── backend/
│   ├── app.py
│   ├── crypto/
│   ├── blockchain/
│   ├── uploads/
│   ├── keys/
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   └── App.js
│   └── package.json
│
├── ganache/
│   └── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### ✅ 1. Install Dependencies

#### Backend (Flask + Crypto + Web3)
```bash
cd backend
pip install -r requirements.txt
```

#### Frontend (React + Axios)
```bash
cd ../frontend
npm install
npm install axios
```

### ✅ 2. Setup Ganache

1. Download **Ganache GUI** from [https://trufflesuite.com/ganache/](https://trufflesuite.com/ganache/)
2. Start it on port `7545`
3. Copy the **RPC Server URL**: `http://127.0.0.1:7545`
4. Use any private key to import an account into MetaMask

### ✅ 3. Setup MetaMask

1. Install [MetaMask Chrome Extension](https://metamask.io/)
2. Add **Custom Network**:
   - **Network Name**: Ganache
   - **RPC URL**: http://127.0.0.1:7545
   - **Chain ID**: 1337
   - **Currency symbol**: ETH
3. Import an account from Ganache using the provided private key

### ✅ 4. Deploy Smart Contract via Remix

1. Open [Remix IDE](https://remix.ethereum.org/)
2. Create file: `SmartContract.sol` → paste the contract code
3. Compile using Solidity 0.8.x compiler
4. Deploy using MetaMask (Injected Web3)
5. Copy the deployed **contract address**

### ✅ 5. Configure `.env` File

Create `.env` file in `ganache/`:

```
CONTRACT_ADDRESS=0xYourContractAddressHere
RPC_URL=http://127.0.0.1:7545
PRIVATE_KEY=0xYourGanachePrivateKeyHere
```

Update `contract.py` to load this `.env` securely.



---

## 🔐 Key File Descriptions

| File/Folder              | Description |
|--------------------------|-------------|
| `aes_utils.py`           | AES-GCM encryption/decryption for files |
| `rsa_utils.py`           | RSA key generation and AES key encryption |
| `signature_utils.py`     | RSA-PSS based digital signature utilities |
| `contract.py`            | Smart contract interaction via Web3.py |
| `SmartContract.sol`      | Solidity contract for file hash registry |
| `app.py`                 | Flask backend with upload, download, verify APIs |
| `UploadForm.js`          | React component for file upload |
| `DownloadForm.js`        | React form for file decryption |
| `VerifyForm.js`          | React form for hash-based integrity check |

---

## 🚀 How to Run the Full System

### ✅ Backend (Flask)
```bash
cd backend
python app.py
```

### ✅ Frontend (React)
```bash
cd frontend
npm start
```

### ✅ Upload a File
- Visit [http://localhost:3000](http://localhost:3000)
- Upload form returns encrypted AES key, nonce, tag, and signature

### ✅ Download a File
- Provide file_id and metadata from upload response
- React UI calls Flask to decrypt and download the file

### ✅ Verify a File
- Enter file_id in Verify form
- Compares stored blockchain hash with local file

---

## 🔐 Security Highlights

- AES-256-GCM encryption with authenticated tags
- RSA 2048-bit encryption for AES key sharing
- Digital signature via RSA-PSS to ensure authenticity
- Blockchain (Ganache + Solidity) used for tamper-proof verification
- End-to-end cryptographic assurance

---

## 📌 Recommendations for Deployment

- Store files on IPFS or S3 instead of local filesystem
- Use HTTPS in production
- Use PostgreSQL/MongoDB for audit logs and metadata
- Deploy to testnet (Sepolia/Mumbai) instead of Ganache for public testing
- Use Hardhat or Truffle for CI/CD blockchain deployment

---
## 🙋‍♂️ Help & Contact

If you encounter any issues while setting up or running the project — whether it's related to dependencies, environment configuration, smart contract deployment, or blockchain interaction — feel free to reach out for support.

### 📧 Contact

**Rishu Jaiswal**  
📩 Email: [jaiswal733rishu@gmail.com](mailto:jaiswal733rishu@gmail.com)  
📞 Phone: +91-9113308603
📱 WhatsApp: [Click to Chat](https://wa.me/+91-9113308603)

## 🧑‍💻 Author & License

Created with dedication 💡 by 
- **Rishu Jaiswal** 
- **Ashish Paul**
- **Ashish Babu**
- **Ravi Charan**

This project is open-source — you are free to use, modify, and share it with attribution.
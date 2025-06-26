from flask_cors import CORS
from pyngrok import ngrok
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
from io import BytesIO
from crypto import aes_utils, rsa_utils, signature_utils
from blockchain import contract
import hashlib, os, binascii

app = Flask(__name__)
CORS(app)  # ✅ enable CORS
UPLOAD_FOLDER = "backend/uploads"
KEY_FOLDER = "backend/keys"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ========== Upload Route ==========
@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    user = request.form.get("user")  # e.g. "alice"
    
    if not file or not user:
        return jsonify({"error": "Missing file or user name"}), 400

    file_data = file.read()
    file_id = secure_filename(file.filename)

    # Step 1: Encrypt file with AES
    aes_key, nonce, tag, ciphertext = aes_utils.encrypt_file(file_data)

    # Step 2: Encrypt AES key with receiver's public RSA key
    enc_key = rsa_utils.encrypt_key(aes_key, f"{KEY_FOLDER}/{user}_public.pem")

    # Step 3: Sign the ciphertext
    signature = signature_utils.sign_data(ciphertext, f"{KEY_FOLDER}/{user}_private.pem")

    # Step 4: Compute SHA256 file hash
    file_hash = hashlib.sha256(ciphertext).hexdigest()

    # Step 5: Register file hash on blockchain
    tx_hash = contract.register_file(file_id, file_hash)

    # Step 6: Save encrypted file
    with open(f"{UPLOAD_FOLDER}/{file_id}.bin", "wb") as f:
        f.write(ciphertext)

    return jsonify({
        "status": "Success",
        "file_id": file_id,
        "file_hash": file_hash,
        "enc_key": enc_key.hex(),
        "nonce": nonce.hex(),
        "tag": tag.hex(),
        "signature": signature.hex(),
        "tx_hash": tx_hash
    })

# ========== Download + Decrypt + Verify + Blockchain Check ==========
@app.route("/download", methods=["POST"])
def download_file():
    file_id = request.form.get("file_id")
    enc_key = request.form.get("enc_key")
    nonce = request.form.get("nonce")
    tag = request.form.get("tag")
    signature = request.form.get("signature")
    user = request.form.get("user")

    if not all([file_id, enc_key, nonce, tag, signature, user]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        enc_key = bytes.fromhex(enc_key)
        nonce = bytes.fromhex(nonce)
        tag = bytes.fromhex(tag)
        signature = bytes.fromhex(signature)
    except binascii.Error:
        return jsonify({"error": "Invalid hex format in input"}), 400

    file_path = f"{UPLOAD_FOLDER}/{file_id}.bin"
    if not os.path.exists(file_path):
        return jsonify({"error": "Encrypted file not found"}), 404

    with open(file_path, "rb") as f:
        ciphertext = f.read()

    try:
        # Step 1: Decrypt AES key
        aes_key = rsa_utils.decrypt_key(enc_key, f"{KEY_FOLDER}/{user}_private.pem")

        # Step 2: Decrypt the file
        decrypted_data = aes_utils.decrypt_file(ciphertext, aes_key, nonce, tag)

        # Step 3: Verify signature
        is_valid = signature_utils.verify_signature(ciphertext, signature, f"{KEY_FOLDER}/{user}_public.pem")
        if not is_valid:
            return jsonify({"error": "Signature verification failed"}), 403

        # Step 4: Verify blockchain hash
        computed_hash = hashlib.sha256(ciphertext).hexdigest()
        blockchain_hash, _, _ = contract.get_file_metadata(file_id)

        if computed_hash != blockchain_hash:
            return jsonify({
                "error": "Blockchain hash mismatch. File may be tampered.",
                "expected": blockchain_hash,
                "actual": computed_hash
            }), 409

        # Step 5: Return decrypted file
        return send_file(BytesIO(decrypted_data),
                         as_attachment=True,
                         download_name=file_id,
                         mimetype='application/octet-stream')

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@app.route("/verify", methods=["POST"])
def verify_file():
    file_id = request.form.get("file_id")
    if not file_id:
        return jsonify({"error": "file_id is required"}), 400

    # Step 1: Load encrypted file
    file_path = f"{UPLOAD_FOLDER}/{file_id}.bin"
    if not os.path.exists(file_path):
        return jsonify({"error": "Encrypted file not found"}), 404

    with open(file_path, "rb") as f:
        ciphertext = f.read()

    # Step 2: Compute hash
    computed_hash = hashlib.sha256(ciphertext).hexdigest()

    # Step 3: Fetch on-chain hash
    try:
        blockchain_hash, uploader, timestamp = contract.get_file_metadata(file_id)
    except Exception as e:
        return jsonify({"error": f"Blockchain lookup failed: {str(e)}"}), 500

    # Step 4: Compare
    if computed_hash == blockchain_hash:
        return jsonify({
            "status": "VERIFIED ✅",
            "file_id": file_id,
            "computed_hash": computed_hash,
            "blockchain_hash": blockchain_hash,
            "uploader": uploader,
            "timestamp": timestamp
        }), 200
    else:
        return jsonify({
            "status": "TAMPERED ❌",
            "file_id": file_id,
            "computed_hash": computed_hash,
            "blockchain_hash": blockchain_hash,
            "uploader": uploader,
            "timestamp": timestamp
        }), 409
    

if __name__ == "__main__":
    # app.run(debug=True, port=5000)
    public_url = ngrok.connect(5000)
    print(" * ngrok tunnel available at:", public_url)
    app.run(port=5000)
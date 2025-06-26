from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

KEY_DIR = "backend/keys"

def generate_keys(path=KEY_DIR, name="user"):
    os.makedirs(path, exist_ok=True)
    private_path = f"{path}/{name}_private.pem"
    public_path = f"{path}/{name}_public.pem"

    if os.path.exists(private_path) and os.path.exists(public_path):
        return  # Keys already exist, no need to regenerate

    key = RSA.generate(2048)
    with open(private_path, "wb") as f:
        f.write(key.export_key())
    with open(public_path, "wb") as f:
        f.write(key.publickey().export_key())

def encrypt_key(aes_key, public_key_path):
    if not os.path.exists(public_key_path):
        user = os.path.basename(public_key_path).split("_")[0]
        generate_keys(KEY_DIR, user)

    key = RSA.import_key(open(public_key_path, "rb").read())
    cipher = PKCS1_OAEP.new(key)
    return cipher.encrypt(aes_key)

def decrypt_key(enc_key, private_key_path):
    if not os.path.exists(private_key_path):
        user = os.path.basename(private_key_path).split("_")[0]
        generate_keys(KEY_DIR, user)

    key = RSA.import_key(open(private_key_path, "rb").read())
    cipher = PKCS1_OAEP.new(key)
    return cipher.decrypt(enc_key)

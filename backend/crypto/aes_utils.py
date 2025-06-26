from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_file(data):
    key = get_random_bytes(32)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return key, cipher.nonce, tag, ciphertext

def decrypt_file(enc_data, key, nonce, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    return cipher.decrypt_and_verify(enc_data, tag)

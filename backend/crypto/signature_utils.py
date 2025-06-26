from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

def sign_data(data, private_key_path):
    key = RSA.import_key(open(private_key_path, "rb").read())
    h = SHA256.new(data)
    return pss.new(key).sign(h)

def verify_signature(data, signature, public_key_path):
    key = RSA.import_key(open(public_key_path, "rb").read())
    h = SHA256.new(data)
    try:
        pss.new(key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

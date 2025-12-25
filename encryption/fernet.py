import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend



def derive_fernet_key(password: str, salt: bytes = None) -> tuple[bytes, bytes]:

    if salt is None:
        salt = os.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390_000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt



# ENCRYPT
def fet_encrypt():
    # USER ENTERS PASSWORD (NOT RAW KEY)
    password = input("Enter password: ")
    if password == None:
        password = Fernet.generate_key()
    else:
        pass
    # DERIVE FERNET KEY
    key, salt = derive_fernet_key(password)
    # CREATE FERNET OBJECT
    f = Fernet(key)
    print("Derived key:", key)
    print("Salt (store this):", salt)
    text = input("Enter text to encrypt: ")
    token = f.encrypt(text.encode())
    print("Encrypted token:", token)

def fet_decrypt():
    token = input("Enter encrypted token: ")
    key = input("Enter Fernet key: ")
    if token or key == None:
        print("these input must be filled!")
    else:
        f = Fernet(key)
        decrypted = f.decrypt(token)
        return decrypted


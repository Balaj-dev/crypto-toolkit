import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def derive_fernet_key(password: str, salt: bytes = None) -> tuple[bytes, bytes]:
    """
    Derive a Fernet-compatible key from a password using PBKDF2HMAC.

    Args:
        password (str): The user-provided password.
        salt (bytes, optional): Random salt. If None, a new 16-byte salt is generated.

    Returns:
        tuple[bytes, bytes]: (fernet_key, salt)
            - fernet_key: 32-byte Fernet key (base64-encoded)
            - salt: 16-byte salt used for key derivation (store for future use)
    """
    if salt is None:
        salt = os.urandom(16)  # generate new random salt

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,             # 32 bytes = Fernet key
        salt=salt,
        iterations=390_000,    # OWASP recommended for 2025
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt


# print(help(Fernet))


import base64 , os
from cryptography.fernet import Fernet

your_32_byte_key = os.urandom(32)
key =  base64.urlsafe_b64encode(your_32_byte_key)
f = Fernet(key)
print(key)
# token = f.encrypt(b"A really secret message. Not for prying eyes.")
#
# print(token)
# print(f.decrypt(token))
# print(key)



def encode_hex(text: str) -> str:
    return text.encode().hex()

def decode_hex(hex_string: str) -> str:
    return bytes.fromhex(hex_string).decode()


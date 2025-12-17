import base64

def urlsafe_encoding(text: str) -> str:
    return base64.urlsafe_b64encode(text.encode()).decode()

def urlsafe_decoding(text: str) -> str:
    return base64.urlsafe_b64encode(text).decode()

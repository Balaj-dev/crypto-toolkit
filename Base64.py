import base64

text = "meow"
# 1. Convert string to bytes
bytes_data = text.encode("utf-8")

# 2. Encode bytes to Base64
encoded_bytes = base64.b64encode(bytes_data)

# 3. Convert Base64 bytes to string for display
encoded_string = encoded_bytes.decode("ascii")

print(f"Original string: {text}")
print(f"Encoded string: {encoded_string}")

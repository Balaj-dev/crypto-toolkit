import base64

def base64_encoding(data_by_user):
    data_by_user = data_by_user.encode("utf-8")
    encoded_bytes = base64.b64encode(data_by_user)
    encoded_string = encoded_bytes.decode("ascii")
    return encoded_string


def base64_decoding(data_by_user):
    data_by_user = data_by_user.encode("utf-8")
    encoded_bytes = base64.b64decode(data_by_user)
    encoded_string = encoded_bytes.decode("ascii")
    return encoded_string


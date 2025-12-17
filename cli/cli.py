import pyfiglet , argparse
from encoding import *

tool_name = pyfiglet.figlet_format("Crypto-Toolkit", font="Standard")
print(tool_name)

print(dir(argparse))

prases = argparse.ArgumentParser(description="used to convert plain text in to cypher text..")


if __name__ == '__main__':
    read_from = input("what you want 32 , 63 , morse, hexa : ")
    if read_from == '32':
        data = input("enter to encode: ")
        print(base32_encoding(data))
    elif read_from == '64':
        data = input("enter to encode: ")
        print(base64_encoding(data))
    elif read_from == 'morse':
        data = input("enter to encode: ")
        print(encode_to_morse(data))
    elif read_from == 'hexa':
        data = input("enter to encode: ")
        print(encode_hex(data))
    else:
        pass

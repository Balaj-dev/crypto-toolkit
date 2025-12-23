import pyfiglet , argparse
from encoding import *
from encryption import *

tool_name = pyfiglet.figlet_format("Crypto-Toolkit", font="Standard")
print(tool_name)

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
parser.add_argument('filename')           # positional argument
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-v', '--verbose',
                    action='store_true')

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

user = input("")
if user == 'e':
    fet_encrypt()
else:
    fet_decrypt()

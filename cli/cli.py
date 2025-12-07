import pyfiglet , argparse
import encoding as encode


tool_name = pyfiglet.figlet_format("Crypto-Toolkit", font="Standard")
print(tool_name)
print(encode.base64_encoding(input("enter something to encode in Base32 format: ")))

# def phrases():

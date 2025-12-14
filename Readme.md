## Encryptor
<h3>Under Construction.....</h3>

<h3>FILE STRUCTURE</h3>

```
crypto-toolkit/
│
├── encoding/                    # Base encoders / decoders
│   ├── __init__.py
│   ├── base64_tools.py
│   ├── base32_tools.py
│   ├── hex_tools.py
│   └── urlsafe_tools.py
│
├── hashing/                     # Hashing + salting
│   ├── __init__.py
│   ├── sha_tools.py
│   ├── md5_tools.py
│   ├── blake2_tools.py
│   ├── salting.py
│   └── peppering.py             # optional, advanced
│
├── encryption/                  # Symmetric + asymmetric encryption
│   ├── __init__.py
│   ├── aes_tools.py             # Symmetric (EASY + recommended)
│   ├── fernet_tools.py          # Even easier AES wrapper via cryptography
│   ├── rsa_tools.py             # Asymmetric (optional, advanced)
│   └── utils.py                 # key generation, file loading, etc.
│
├── cli/                         # Command line interface
│   ├── __init__.py
│   └── cli.py
│
├── web/                         # Flask web app
│   ├── __init__.py
│   ├── web.py                   # main Flask runner
│   ├── routes.py
│   ├── forms.py                 # optional, for WTForms
│   └── templates/
│       ├── index.html
│       └── result.html
│
├── tests/                       # Unit tests
│   ├── test_encoding.py
│   ├── test_hashing.py
│   └── test_encryption.py
│
├── requirements.txt
├── README.md
└── LICENSE

```

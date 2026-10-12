#Since shared secret is generated as: M^c where we choose M, we can simply choose M = 0 and the shared secret becomes 0^c = 0 .
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import hashlib

def encrypt():
    message = b"Initialization Sequence - Code 0"
    key = hashlib.md5(long_to_bytes(0)).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    message = cipher.encrypt(message)
    print(message.hex())

encrypt()

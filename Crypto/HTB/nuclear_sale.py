#In the pcap, a ciphertext is encrypted twice. Using XOR, this generates the plaintext. XOR:ing the ciphertext with the plaintext will return the key, since the plaintext part will be canceled out. XOR:ing the encrypted flag with the key will return the flag.
def xor_encrypt_decrypt(hex_input, hex_key):
    data = bytes.fromhex(hex_input)
    key = bytes.fromhex(hex_key)

    if not key:
        raise ValueError("Key must not be empty")

    result = bytes(byte ^ key[i % len(key)] for i, byte in enumerate(data))
    return result.hex()

# Example usage
encrypted_with_key = "fd034c32294bfa6ab44a28892e75c4f24d8e71b41cfb9a81a634b90e6238443a813a3d34"
decrypted_with_key = "de328f76159108f7653a5883decb8dec06b0fd9bc8d0dd7dade1f04836b8a07da20bfe70"
ciphertext = "6b65813f4fe991efe2042f79988a3b2f2559d358e55f2fa373e53b1965b5bb2b175cf039"
key = xor_encrypt_decrypt(encrypted_with_key, decrypted_with_key)
flag = xor_encrypt_decrypt(ciphertext, key)

print("Flag", bytes.fromhex(flag))

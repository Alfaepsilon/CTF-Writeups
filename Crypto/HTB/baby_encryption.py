import string

def encryption():
    ct = []
    f = open('msg.enc')
    cipher = f.read()
    cipher = [cipher[i:i+2] for i in range(0, len(cipher), 2)]
    for c in cipher:
        #Inverse of 123 mod 256 is 179
        c = bytes.fromhex(c)
        c = int.from_bytes(c)
        ct.append(chr(((c - 18) * 179) % 256))
    return ct

ct = encryption()
ct = ''.join(ct)
print(ct)

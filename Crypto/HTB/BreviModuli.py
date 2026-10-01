#Server uses 100 bit primes, which are very small. Using the Quadratic Sieve, the moduli can be factored easely.
from pwn import *
import time
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
def solution():
    context.log_level = "debug"
    conn = remote('154.57.164.65',31059)
    for i in range(5):
        line = conn.recvuntil(b"-----END PUBLIC KEY-----").decode()
        key = [x for x in line.split("?")[1]]
        key = "".join(key).encode("utf-8")
        print(key)
        key = serialization.load_pem_public_key(key)
        numbers = key.public_numbers()
        N = Integer(numbers.n)
        print(N)
        factors = N.factor(algorithm="qsieve")
        print(factors)
        p = Integer(factors[0][0])    
        q = Integer(factors[1][0])
        conn.sendline(str(int(p)).encode())
        sleep(1)
        conn.sendline(str(int(q)).encode())
    conn.recvall()
solution()

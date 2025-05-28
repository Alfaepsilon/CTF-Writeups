#!/usr/bin/env python3

from pwn import * # pip install pwntools
import json

HOST = "challenge.nahamcon.com"
PORT = 30930

r = remote(HOST, PORT)


def main():
    r.readline()
    line = r.readline()
    r.readline()
    encrypted_flag = line.split(b':')
    encrypted_flag = encrypted_flag[1].decode("utf-8")
    encrypted_bytes = bytearray.fromhex(encrypted_flag)
    r.sendline(encrypted_bytes)
    line = r.readline()
    decrypted_flag = line.split(b':')[1]
    flag = decrypted_flag.decode()
    flag = bytearray.fromhex(flag).decode("utf-8")
    print(flag)


main()

#!/usr/bin/env python3

from pwn import * # pip install pwntools
import json

HOST = "challenge.nahamcon.com"
PORT = 31744

r = remote(HOST, PORT)


def main():
    while(True):
        a = r.readline().decode('utf-8')
        if('flag{' in a):
            print(a)
            #r.close()
            exit
        r.sendline()


main()

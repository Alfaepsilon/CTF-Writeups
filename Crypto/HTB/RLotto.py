from pwn import *
import time
import random
def solution():
    context.log_level = "debug"
    seed = int(time.time())
    conn = remote('154.57.164.82',32364)
    next_five = []
    line = conn.recvuntil(b"Put here the next 5 numbers: ").decode()
    numbers = [int(x) for x in line.split("EXTRACTION: ")[-1].split(' ')[0:5]]
    print(numbers)
    # Initialize the (pseudo)random number generator
    random.seed(seed)
    while True:
        a = 0
        random.seed(seed)
        for i in numbers:
            r = random.randint(1, 90)
            if r == i:
                a += 1
        if a == 5:
            break
        seed += 1
        # Next extraction
       
    solution = ""
    while len(next_five) < 5:
        print("check 2")
        r = random.randint(1, 90)
        if(r not in next_five):
            next_five.append(r)
            solution += str(r) + " "
    answer = b" ".join(str(number).encode() for number in next_five)
    conn.sendline(answer)
    flag = conn.recvall(timeout=3)
    print(flag)
solution()

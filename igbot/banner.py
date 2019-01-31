#!/usr/bin/env python3

import random
import time

author  = 'decoxviii'
version = '31.01.19'

def shuffle(line):
    chars  = ['A', '9', 'X', '$', 'S', '6', 'W', 'Q', 'Z', '0', '1']
    for x in range(0, random.randint(1, 5)):
        aux = random.sample(chars, k=11)
        print("\t{}".format(' '.join(aux)), end="\r")
        time.sleep(0.1)
    print(line)

def print_banner():
    lines = ["\tF 2 R L 5 S G G H / /", 
             "\tS\033[1m I N S T A G R A M\033[0m R", 
             "\tQ 3 0 G 5 & 1 9 2 # W", 
             "\tH $ W 0\033[1m B O T\033[0m 9 1 G M",
             "\t/ / E J R A 0 0 G N S"]

    print("\n\n")
    [shuffle(line) for line in lines]
    print("\n\n\t{}".format(author))
    print("\t{}\n\n".format(version))


#!/usr/bin/env python3

import argparse
from sys import exit

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="number system to convert from")
    parser.add_argument("target", help="number system to convert to")
    parser.add_argument("num", help="the number to convert", type=int)
    args = parser.parse_args()

    n = args.num
    rem = 0
    div = 0
    remainder_arr = []
    hex_letters = ['A', 'B', 'C', 'D', 'E', 'F']
    
    if args.source == "d" or args.source == "dec" or args.source == "decimal":
        pass
    elif args.source == "b" or args.source == "bin" or args.source == "binary":
        pass

    if args.target == "b" or args.target == "bin" or args.target == "binary":
        div = 2
    elif args.target == "h" or args.target == "hex" or args.target == "hexadecimal":
        div = 16
    elif args.target == "o" or args.target == "oct" or args.target == "octal":
        div = 8
    else:
        print(f"Invalid target number system: {args.target}")
        exit(1)

    while n != 0:
        rem = n % div
        if rem > 9:
            rem = hex_letters[rem % 10] 
        remainder_arr.append(rem)
        n //= div

    conv_str = ''.join(map(str, remainder_arr[::-1]))
    print(conv_str)


if __name__ == "__main__":
    cli()

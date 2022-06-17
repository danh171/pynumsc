#!/usr/bin/env python3

import argparse
import enum
from sys import exit

def cli():
    parser = argparse.ArgumentParser()
    # parser.add_argument("source", help="number system to convert from")
    parser.add_argument("target", help="number system to convert to")
    parser.add_argument("num", help="the number to convert")
    args = parser.parse_args()

    decimal_num = 0
    base = 0

    if args.target == "b" or args.target == "bin" or args.target == "binary":
        base = 2
    elif args.target == "h" or args.target == "hex" or args.target == "hexadecimal":
        base = 16
    elif args.target == "o" or args.target == "oct" or args.target == "octal":
        base = 8
    else:
        print(f"Invalid target number system: {args.target}")
        exit(1)
    
    for i, c in enumerate(args.num[::-1]):
        decimal_num += base**i * int(c)

    print(decimal_num)

if __name__ == "__main__":
    cli()

# TODO: Need to account for letters in base 16
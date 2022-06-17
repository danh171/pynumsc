#!/usr/bin/env python3

import argparse
from sys import exit

def cli():
    parser = argparse.ArgumentParser(description="A Simple Command Line Number System Converter")
    parser.add_argument("source", help="number system to convert from")
    parser.add_argument("target", help="number system to convert to")
    parser.add_argument("num", help="the number to convert")
    args = parser.parse_args()
    
    hex_letters = ['A', 'B', 'C', 'D', 'E', 'F']

    if args.source == "d" or args.source == "dec" or args.source == "decimal":
        n = int(args.num)
        rem = 0
        div = 0
        remainder_arr = []

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
    elif args.target == "d" or args.target == "dec" or args.target == "decimal":
        decimal_num = 0
        base = 0
        digit = 0

        if args.source == "b" or args.source == "bin" or args.source == "binary":
            base = 2
        elif args.source == "h" or args.source == "hex" or args.source == "hexadecimal":
            base = 16
        elif args.source == "o" or args.source == "oct" or args.source == "octal":
            base = 8
        else:
            print(f"Invalid source number system: {args.source}")
            exit(1)
        
        for i, c in enumerate(args.num[::-1]):
            if c in hex_letters:
                digit = hex_letters.index(c) + 10
            else:
                digit = int(c)
            decimal_num += base**i * digit

        print(decimal_num)


if __name__ == "__main__":
    cli()

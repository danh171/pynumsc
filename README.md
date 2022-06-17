# PyNumSC: A Simple Command Line Number System Converter

PyNumSC is a CLI application which can be used to convert from decimal to binary, octal, or hexadecimal. It can also be used to convert from binary, octal, or hexadecimal
to decimal.

## Usage

```shell
# convert decimal to hexadecimal:
$ python3 pynumsc.py d h 42
2A

# binary to decimal
$ python3 pynumsc.py bin dec 10011
19

# octal to decimal
$ python3 pynumsc.py octal decimal 17
15

# show help message
$ python3 pynumsc.py -h
usage: pynumsc.py [-h] source target num

A Simple Command Line Number System Converter

positional arguments:
  source      number system to convert from
  target      number system to convert to
  num         the number to convert

optional arguments:
  -h, --help  show this help message and exit
```

If `source` is `decimal`, `dec`, or `d`, the following `target` number systems are available:

- Binary: `binary`, `bin`, or `b`

- Octal: `octal`, `oct`, or `o`

- Hexadecimal: `hexadecimal`, `hex`, or `h`

If `target` is `decimal`, `dec`, or `d`, the following `source` number systems are available:

- Binary: `binary`, `bin`, or `b`

- Octal: `octal`, `oct`, or `o`

- Hexadecimal: `hexadecimal`, `hex`, or `h`

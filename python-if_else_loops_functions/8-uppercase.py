#!/usr/bin/python3
def uppercase(s):
    for c in s:
        upper_char = chr(ord(c) - 32) if "a" <= c <= "z" else c
        print("{:s}".format(upper_char), end="")
    print()

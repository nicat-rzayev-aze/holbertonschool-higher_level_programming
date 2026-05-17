#!/usr/bin/python3
def uppercase(str):
    biggy = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            biggy += chr(ord(c) - 32)
        else:
            biggy += c
    print("{}".format(biggy))

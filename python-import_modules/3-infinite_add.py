#!/usr/bin/python3
import sys

if __name__ == "__main__":
    toplam = 0

    for arguman in sys.argv[1:]:
        toplam += int(arguman)

    print("{}".format(toplam))

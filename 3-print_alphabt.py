#!/usr/bin/python3
print("".join("{:c}".format(i) for i in range(97, 123) if i != 101 and i != 113), end="")

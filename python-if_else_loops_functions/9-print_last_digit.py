#!/usr/bin/python3
def print_last_digit(number):
    if number != 0:
        print(abs(number) % 10, end = "")
    else:
        print("0", end = "")
    return print(abs(number) % 10, end = "")

#!/usr/bin/env python3


import sys


def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        return print("ERROR")
    num = int(sys.argv[1])
    if num == 0:
       return print("I'm Zero.")
    return print("I'm Even") if num % 2 else print("I'm Odd.")


if __name__ == '__main__':
    main()

import sys


def main():
    n = len(sys.argv)
    if n <= 1:
        return
    for x in range(1, n):
        print(sys.argv[x][::-1], end='')
        if x != (n - 1):
            print(" ", end='')


if __name__ == '__main__':
    main()

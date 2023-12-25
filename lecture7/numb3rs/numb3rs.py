import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    data = ip.strip().split('.')
    if len(data) != 4:
        return False
    try:
        for i in data:
            if int(i) < 0 or int(i) > 255:
                return False
        return True
    except ValueError:
        return False


...


if __name__ == "__main__":
    main()

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    inputstr = s.strip()
    pattern = r'(<iframe)?.*src="http[s]?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+).*("></iframe>)?'
    matches = re.match(pattern, inputstr)
    if matches:
        return 'https://youtu.be/' + matches.groups()[-2]



if __name__ == "__main__":
    main()

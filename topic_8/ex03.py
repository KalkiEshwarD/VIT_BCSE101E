import re


def main():
    match = re.search(r"(25[0-5]|2[0-4]\d|1\d\d|\d\d|\d)\.(25[0-5]|2[0-4]\d|1\d\d|\d\d|\d)\.(25[0-5]|2[0-4]\d|1\d\d|\d\d|\d)\.(25[0-5]|2[0-4]\d|1\d\d|\d\d|\d)", input())
    if match:
        print(match.group())
    else:
        print('Invalid IPv4 Address')


if _name_ == "_main_":
    main()

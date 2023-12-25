import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    inputstr = s.strip()
    pattern = r'(0?[1-9]|1[0-2])\.?:?\.?([0-5]{1}[0-9]{1})? (AM|PM) to (0?[1-9]|1[0-2])\.?:?\.?([0-5]{1}[0-9]{1})? (AM|PM)'
    matches = re.match(pattern, inputstr)
    if matches:
        result = matches.groups()
        #  print(result)
        time1 = convert_time(result[0],result[1],result[2])
        time2 = convert_time(result[3],result[4],result[5])
        return f'{time1} to {time2}'
    else:
        raise ValueError

def convert_time(hour,min,x):
        # print(min is None)
        min = f'{int(min):02}' if min else '00'
        if hour == "12":
            if x == "AM":
                hour = "00"
            else:
                hour = "12"
        else:
            if x == "AM":
                hour = f'{int(hour):02}'
            else:
                hour = f'{int(hour)+12}'
        return f'{hour}:{min}'






if __name__ == "__main__":
    main()

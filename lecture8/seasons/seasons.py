from datetime import date
import inflect
import re
import operator
import sys
p = inflect.engine()

def main():
    birth = input('Date of Birth: ')
    if check_formt(birth):
        howlong = operator.sub(date.today(), date.fromisoformat(birth))
        print(convert(howlong.days))
    else:
        sys.exit('Invalid date')


def convert(s):
    minutes = s * 24 * 60
    return f'{p.number_to_words(str(minutes), andword='').capitalize()} minutes'
    # return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"

def check_formt(s):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    result = re.match(pattern, s.strip())
    if result:
        return True
    else:
        return False


if __name__ == "__main__":
    main()

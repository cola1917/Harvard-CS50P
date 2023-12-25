# while True:
#     try:
#         fraction = input('Fraction: ')
#         index = fraction.find('/')
#         if index == -1:
#             continue
#         x,o,n = fraction[:index],fraction[index],fraction[index+1:]
#         if n == '0':
#             continue
#         elif not x.isdigit() or not n.isdigit():
#             continue
#         x,n = int(x), int(n)
#         if x > n:
#             continue
#         result = round(x/n,2)
#         # return result)
#         if result <= 0.01:
#             return 'E')
#             break
#         elif result >= 0.99:
#             return 'F')
#             break
#         elif result >= 0:
#             return  f'{int(result * 100)}%')
#             break
#     except (ValueError, ZeroDivisionError):
#         pass

def main():
    fraction = input('Fraction: ')
    print(gauge(convert(fraction)))


def convert(fraction):
    index = fraction.find('/')
    if index == -1:
        raise ValueError
    x,o,n = fraction[:index],fraction[index],fraction[index+1:]
    if n == '0':
        raise ZeroDivisionError
    elif not x.isdigit() or not n.isdigit():
        raise ValueError
    x,n = int(x), int(n)
    if x > n:
        raise ValueError
    return round(x/n,2) * 100


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99 and percentage <= 100:
        return 'F'
    elif percentage > 100:
        raise ValueError
    elif percentage > 1:
        return  f'{int(percentage)}%'


if __name__ == "__main__":
    main()

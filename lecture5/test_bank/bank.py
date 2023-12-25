# result = input('Greeting: ').lower().strip()
# if result[:5] == 'hello':
#     print("$0")
# elif result[0] == 'h':
#     print("$20")
# else:
#     print('$100')
def main():
    result = value(input('Greeting: '))
    print(f'${result}')



def value(greeting):

    greeting = greeting.lower().strip()
    if greeting[:5] == 'hello':
        return 0
    elif greeting[0] == 'h':
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

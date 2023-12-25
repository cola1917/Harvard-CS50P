import random


def main():
    score = 0
    n = get_level()
    for i in range(10):
        numberlist = [generate_integer(n), generate_integer(n)]
        count = 0
        while True:
            if count < 3:
                try:
                    result = int(input(f'{numberlist[0]} + {numberlist[1]} = '))
                    if result == numberlist[0] + numberlist[1]:
                        score+=1
                        break
                    else:
                        count+=1
                        print('EEE')
                except ValueError:
                    count+=1
                    print('EEE')
            else:
                print(f'{numberlist[0]} + {numberlist[1]} = {numberlist[0] + numberlist[1]}')
                break


    print(f'Score: {score}')


def get_level():
    while True:
        try:
            number = int(input('Level: '))
            if number > 0 and number < 4:
                break
        except ValueError:
            continue
    return number

# test fail, but it is correct
# def generate_integer(level):
#     return [int(random.random() * 10 ** level) for i in range(2)]
def generate_integer(level):
    if level == 1:
        start = 0
        stop = 10
    else:
        start = 10 ** (level-1)
        stop = 10 ** level
    rand_int = random.randrange(start,stop,1)
    return rand_int



if __name__ == "__main__":
    main()

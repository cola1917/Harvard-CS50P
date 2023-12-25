import random

while True:
    try:
        level = int(input('Level: '))
        n = random.randint(1, level + 1)
        break
    except ValueError:
        continue
while True:
    try:
        guess = int(input('Guess: '))
        if guess <= 1:
            continue
        if guess > n:
            print('Too large!')
            continue
        elif guess < n:
            print('Too small!')
            continue
        else:
            print('Just right!')
            break
    except ValueError:
        continue

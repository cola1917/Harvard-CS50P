need_coin = 50
while need_coin > 0:
    print(f'Amount Due: {need_coin}')
    input_coin = int(input('Insert Coin: '))
    if input_coin == 25:
        need_coin -= 25
    elif input_coin == 10:
        need_coin -= 10
    elif input_coin == 5:
        need_coin -= 5

print(f'Change Owed: {-need_coin}')
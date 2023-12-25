def main():
    time = input('What time is it? ')
    result = convert(time)
    # print(result)
    # if 7 <= hour <= 8:
    #     if minute == 0:
    #         print('breakfast time')
    #     elif hour == 7:
    #         print('breakfast time')
    # elif 12 <= hour <= 13:
    #     if minute == 0:
    #         print('lunch time')
    #     elif hour == 12:
    #         print('lunch time')
    # elif 18 <= hour <= 19:
    #     if minute == 0:
    #         print('dinner time')
    #     elif hour == 18:
    #         print('dinner time')
    if 7 <= result <= 8:
        print('breakfast time')
    elif 12 <= result <= 13:
        print('lunch time')
    elif 18 <= result <= 19:
        print('dinner time')


def convert(time):
    index = time.find(':')
    if index == -1:
        index = time.find('.')
        hour = int(time[:index])
        minute = float(time[index + 1: index + 3])
    else:
        hour = int(time[:index])
        minute = int(time[index + 1: index + 3]) / 6
    if time.endswith('a.m.'):
        pass
    elif time.endswith('p.m.'):
        hour+=12

    return hour + minute / 10

if __name__ == "__main__":
    main()
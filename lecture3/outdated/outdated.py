month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    inputstr = input('Date: ')
    # print(inputstr)
    if inputstr.find('/') != -1:
        input_list = inputstr.split('/')
        # print(input_list)
        try:
            day = int(input_list[1])
            month = int(input_list[0])
            year = int(input_list[2])
        except ValueError:
            continue
        if day > 31 or day < 1:
            continue
        elif month > 12 or month < 1:
            continue
        print(f'{year}-{month:02}-{day:02}')
        break
    elif inputstr.find(',') != -1:
        input_list = inputstr.split(',')
        month_day = input_list[0].split()
        # print(input_list,month_day)
        try:
            day = int(month_day[1])
            month = month_day[0]
            year = int(input_list[1])
        except ValueError:
            continue
        if month.capitalize() not in month_list:
            continue
        elif day > 31 or day < 1:
            continue
        print(f'{year}-{month_list.index(month.capitalize()) + 1:02}-{day:02}')
        break





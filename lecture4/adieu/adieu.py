begin = 'Adieu, adieu, '
namelist = []
while True:
    try:
        names = input('Name: ').lower()
        if len(names) > 0:
            item = names.split(' ')
            namelist.extend(item)
    except EOFError:
        break
# print(namelist)
namelist = [i.capitalize() for i in namelist[:]]
count = len(namelist)
if count == 1:
    namelist[0] = 'to ' + namelist[0]
elif count == 2:
    namelist[0] = 'to ' + namelist[0] + ' and ' + namelist[1]
    miss = namelist.pop()
else:
    namelist[0] = 'to ' + namelist[0]
    namelist[-1] = 'and ' + namelist[-1]

# print(namelist)
print(begin + ', '.join(namelist))



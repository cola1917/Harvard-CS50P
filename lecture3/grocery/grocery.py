totalstr =  ''
totallist = []
while True:
    try:
        item = input().lower()
        totalstr += item
        if item not in totallist:
            totallist.append(item)
    except EOFError:
        break
totallist.sort()
# print(totallist)
for i in totallist:
    print(f'{totalstr.count(i)} {i.upper()}')

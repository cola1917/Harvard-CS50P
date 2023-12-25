filename = input('type file name please: ').lower()
index = filename.rfind('.')
strend = filename[index+1:]
strlist = ''.join([i for i in strend if i.isalpha()])
strend = strlist
# print(strlist)
typelist = ['gif', 'jpg', 'jpeg', 'png', 'pdf', 'txt', 'zip']
if strend in typelist:
    if strend == 'pdf':
        print('application/' + strend, end='')
    elif strend == 'txt':
        print('text/plain', end='')
    elif strend == 'zip':
        print('application/' + strend, end='')
    elif strend == 'jpeg':
        print('image/jpeg', end='')
    elif strend == 'jpg':
        print('image/jpeg', end='')
    else:
        print('image/' + strend, end='')
else:
    print('application/octet-stream', end='')
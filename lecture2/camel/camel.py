astr = input('camelCase: ')
print('snake_case: ' + ''.join(['_' + i.lower() if 'A' <= i <= 'Z' else i for i in astr]))
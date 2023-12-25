import emoji

emostr = input('Input: ')
print(f'Output: {emoji.emojize(emostr, language='alias')}')

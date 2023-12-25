answer = input('What is the Answer to the Great Question of Life, the Universe, and Everything?')
answer_list = ['42','forty-two','forty two']
if answer.strip().lower() in answer_list:
    print('yes')
else:
    print('no')
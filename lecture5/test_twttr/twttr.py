vowels = ['a', 'e', 'i', 'o', 'u']

def main():
    word = input('Input: ')
    return shorten(word)


def shorten(word):
    return 'Output: ' + ''.join([i for i in word if i.lower() not in vowels])


if __name__ == "__main__":
    main()

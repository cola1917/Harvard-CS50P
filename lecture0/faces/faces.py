def convert(somthing):
    result = somthing.replace(':)', '🙂')
    result = result.replace(':(', '🙁')
    return result


def main():
    inputcontent = input('type something with :) or :(\n')
    result = convert(inputcontent)
    print(result)

main()
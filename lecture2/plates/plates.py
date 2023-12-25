def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2  or len(s) > 6:
        return False
    elif not s[:2].isalpha():
        return False
    num_index_list = [i for i in s if i.isdigit()]
    # print(num_index_list)
    if len(num_index_list) > 0:
        if num_index_list[0] == '0':
            return False
        elif not s[s.index(num_index_list[0]):].isdigit():
            return False
    return True




if __name__ == "__main__":
    main()

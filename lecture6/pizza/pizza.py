import sys
import os
import tabulate
import csv

def main():
    if len(sys.argv) != 2:
        print('Too few command-line arguments')
        sys.exit(1)
    path = sys.argv[1]
    if check_is_file(path):
        if check_csv_file(path):
            print(show_csv_file(path))
        else:
            print('Not a CSV file')
            sys.exit(1)
    else:
        print('File does not exist')
        sys.exit(1)
def check_is_file(path):
    return os.path.isfile(path)
def check_csv_file(path):
    return os.path.basename(path).endswith('.csv')
def show_csv_file(path, type='asciidoc'):
    content = []
    with open(path, 'r', encoding='utf-8') as f:
        return tabulate.tabulate(csv.DictReader(f), headers='keys', tablefmt="grid")
        # for row in reader:
        #     content.append({"value1": row[0], "value2": row[1], "value3": row[2]})
    # return tabulate.tabulate(content, tablefmt="grid")

if __name__ == "__main__":
    main()

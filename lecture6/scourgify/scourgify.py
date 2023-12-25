import sys
import csv
count_argv = len(sys.argv)
if count_argv < 3:
    sys.exit('Too few command-line arguments')
elif count_argv > 3:
    sys.exit('Too many command-line arguments')
new_content = []
try:
    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for i in reader:
            new_content.append({'first':i['name'].split(',')[1].strip(), 'last':i['name'].split(',')[0].strip(), 'house':i['house']})
    # print(new_content)

    with open(sys.argv[2], 'w', encoding='utf-8', newline="") as file:
        fieldnames = new_content[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in new_content:
            writer.writerow(i)
except FileNotFoundError:
    sys.exit("File does not exist.")

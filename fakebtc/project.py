import requests
from pyfiglet import Figlet
import sys
import datetime
import csv
from util import simpleToolSql
from util import PDF
from fpdf.enums import XPos, YPos

dbTool = simpleToolSql()
# init db
init_sql = 'create table if not exists record(id integer PRIMARY KEY autoincrement,price REAL NOT NULL,amount REAL NOT NULL,time TEXT NOT NULL)'
dbTool.execute(init_sql)
find_data_sql = 'select * from record;'
db_source = dbTool.query(find_data_sql)
# print(db_source)
transactionHistorys = []

def main():
    run()

def run():

    # hello stage
    print(show_hello())
    price = get_btc_price()
    print(f'{datetime.date.today()} one BTC is {price} $')

    # ready to enter
    mainMenuOption = [('1', 'Overview'), ('2', 'Purchase'), ('3', 'ExportData'), ('4', 'Exit')]
    subMenuOptionData = [('1', 'To CSV'), ('2', 'To PDF'), ('3', 'Back')]

    # enter main menu
    while True:
        print()
        for item in mainMenuOption:
            print(f'₿ {item[0]}: {item[1]}')
        selected = input('Press: ')
        if selected == '1':
            print("You selected Overview.")
            print(overview(price))
            continue
        elif selected == "2":
            print("You selected Purchase.")
            while True:
                try:
                    amount = float(input('How many do you want? '))
                    purchase(price, amount)
                    break
                except ValueError:
                    continue
            continue
        elif selected == "3":
            print("You selected ExportData.")
            while True:
                print()
                for subItem in subMenuOptionData:
                    print(f'💾 {subItem[0]}: {subItem[1]}')
                subSelected = input('Press: ')
                if subSelected == '1':
                    print("Export to CSV.")
                    print(data_to_csv())
                    continue
                elif subSelected == '2':
                    print("Export to PDF.")
                    print(data_to_pdf())
                    continue
                elif subSelected == '3':
                    print("Back to main menu.")
                    break
                else:
                    print("Invalid choice. Try again.")
                    continue
            continue
        elif selected == "4":
            sys.exit("Bye.")
        else:
            print("Invalid choice. Try again.")
            continue



def show_hello(text='Welcome to FakeBTC ! ', font='slant'):
    figlet = Figlet()
    figlet.setFont(font=font)
    return figlet.renderText(text)


def get_btc_price():
    api = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    data = requests.get(api).json()
    return data['bpi']['USD']['rate_float']

def purchase(price, amount=0):
    if not amount:
        return f'{amount} do not need purchase'
    record = parser(price, amount)
    write_to_db(record)
    if amount > 0:
        transactionHistorys.append(record)
        return f'{amount} BTC has purchased, cost {record['price'] * record['amount']}$'
    else:
        transactionHistorys.append(record)
        return f'{-amount} BTC has sold, get {record['price'] * record['amount']}$'

def parser(price, amount):
    result = {}
    result['price'] = price
    result['amount'] = amount
    result['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return result

def overview(price=None):
    db_source = dbTool.query(find_data_sql)
    formal_to_record(db_source)
    if transactionHistorys and price:
        count = sum([item['amount'] for item in transactionHistorys])
        totalCost = sum([item['amount'] * item['price'] for item in transactionHistorys])
        nowMoney = count * price
        return f'You have {count} BTC, cost {totalCost:.4f}$, now they are {nowMoney:.4f}$'
    return 'no record'

def data_to_csv():
    db_source = dbTool.query(find_data_sql)
    formal_to_record(db_source)
    if transactionHistorys:
        path = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S") + '_data' + '.csv'
        with open(path, 'w', encoding='utf-8') as file:
            fieldnames = transactionHistorys[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in transactionHistorys:
                writer.writerow(row)
            return 'Success!'
    else:
        return 'no record'

def data_to_pdf():
    db_source = dbTool.query(find_data_sql)
    formal_to_record(db_source)
    if transactionHistorys:
        pdf = PDF()
        pdf.add_page()
        pdf.set_font('Times', '', 12)
        for line in transactionHistorys:
            text = f'{line['time']}, {line['price']}, {line['amount']}'
            pdf.cell(0, 10, text, 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Output the PDF to a file
        path = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S") + '_data' + '.pdf'
        pdf.output(path)
        return 'Success!'
    else:
        return 'no record'
def write_to_db(record):
    sql = f"INSERT INTO record (price, amount, time) VALUES({record['price']}, {record['amount']}, '{record['time']}');"
    # print(sql)
    dbTool.execute(sql)

def formal_to_record(db_data):
    transactionHistorys.clear()
    [transactionHistorys.append({'price': item[1], 'amount': item[2], 'time': item[3],}) for item in db_data]
    # print(transactionHistorys)






if __name__ == "__main__":
    main()

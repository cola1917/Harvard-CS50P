import requests
import sys

try:
    price = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
except requests.RequestException:
    print('request error')
# print(price)
if len(sys.argv) == 2:
    try:
        amount = float(sys.argv[1])
        amount = amount * price['bpi']['USD']['rate_float']
        print(f"${amount:,.4f}")
    except ValueError:
        print('Command-line argument is not a number')
        sys.exit(1)
else:
    print('Missing command-line argument')
    sys.exit(1)

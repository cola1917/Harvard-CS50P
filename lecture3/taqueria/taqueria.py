menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
new_menu = {k.lower():menu[k] for k in menu}
# print(new_nemu)
total = 0.00
while True:
    try:
        entree = input('Item: ').lower()
        if entree in new_menu:
            total += new_menu[entree]
            print('Total: ${:.2f}'.format(total))
            continue
    except EOFError:
        break

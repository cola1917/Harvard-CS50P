fruit_Calories = {}
fruit_Calories['apple'] = 130
fruit_Calories['avocado'] = 50
fruit_Calories['sweet cherries'] = 100
fruit_Calories['kiwifruit'] = 90
fruit_Calories['pear'] = 100
# fruit_Calories['sweet cherries'] = 100
fruit = input('Item: ').lower()
if fruit in fruit_Calories:
    print(f'Calories: {fruit_Calories[fruit]}')
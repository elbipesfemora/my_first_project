from datetime import datetime


product_list = []

while True:
    user_input = input('Введите данные о покупке в формате "продукт:цена:категория" '
    '(для закршения введите "стоп"):\n')
    if user_input.lower() == 'стоп':
        break
    part = user_input.split(':')
    if len(part) == 3:
        product = part[0]
        str_cost = part[1]
        category = part[2]
        if str_cost.isdigit():
            cost = int(str_cost)
            product_list.append((product, cost, category))
        else:
            print(f'Цена в записи должна быть числом, вы ввели {user_input}.')
    else:
        print('Некорректный формат записи.')

category_dict = {}

for item in product_list:
    product, cost, category = item
    if category not in category_dict:
        category_dict[category] = {'item' : [], 'total cost' : 0}
    category_dict[category]['item'].append((product, cost))
    category_dict[category]['total cost'] += cost


all_purchases = len(product_list)
all_cost = sum(item[1] for item in product_list)
midle_cost = all_cost / all_purchases if all_purchases > 0 else 0 

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print('-' * 42)
print(current_time)
print('-' * 42)

for category, data in category_dict.items():
    item = data['item']
    total_price = data['total cost']
    midle_pice = total_price / len(item) if len(item) > 0 else 0 
    print(f'категория: {category}')
    print(f'общая стоимость: {total_price} рублёв')
    print(f'средняя стоимость: {midle_pice:.2f} рублёв')
    print('список покупок: ')
    for product, cost in item:
        print(f' - {product}: {cost} рублёв.')
    

'''for category, item in category_dict.items():
    print(f'{category}: ')
    for product, cost in item:
        print(f' - {product}: {cost} рублёв.')'''





# git add .
#git commit -m "какой-то текст"
#git push
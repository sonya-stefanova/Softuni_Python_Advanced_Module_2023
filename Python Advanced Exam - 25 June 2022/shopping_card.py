def shopping_cart(*args):
    result = ''
    products_limit = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2,
    }
    meals_dict = {
        'Soup': set(),
        'Pizza': set(),
        'Dessert': set()
    }
    for arg in args:
        if arg == 'Stop':
            break
        type_of_meal, product = arg
        if len(meals_dict[type_of_meal])<products_limit[type_of_meal]:
            meals_dict[type_of_meal].add(product)
        else:
            continue

    counter = 0
    for k, v in meals_dict.items():
        if len(v)==0:
            counter+=1

    if counter == 3:
        result = "No products in the cart!"
    else:
        for meal, products in sorted(meals_dict.items(), key=lambda x: (-len(x[1]), x[0])):
            result += f'{meal}:\n'
            for product in sorted(products):
                result += f' - {product}\n'
    return result

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))



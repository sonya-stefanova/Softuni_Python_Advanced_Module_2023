def shop_from_grocery_list(budget, grocery_list, *args):
    result = ''
    remaining = ''
    bought_products = set()
    budget = int(budget)
    budget_not_enough = False

    for arg in args:
        product = arg[0]
        price = float(arg[1])
        if product not in grocery_list:
            continue

        if budget - price >=0:
            budget-=price
            bought_products.add(product)
            grocery_list = [i for i in grocery_list if i != product]
        else:
            budget_not_enough=True
            break

    if len(grocery_list) == 0:
        result = f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        result = f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."

    return result



print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

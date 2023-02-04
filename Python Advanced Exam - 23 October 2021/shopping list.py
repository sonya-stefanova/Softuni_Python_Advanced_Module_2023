def shopping_list(budget: int, **kwargs):
    result = []

    if budget < 100:
        result = ["You do not have enough budget."]

    else:
        for product, data in kwargs.items():
            total = 0
            if len(result)==5:
                break
            price = float(data[0])
            quantity = float(data[1])
            total = price * quantity

            if total > budget:
                continue
            else:
                result.append(f"You bought {product} for {total:.2f} leva.")
                budget-=total



    return "\n".join(result)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))




def stock_availability(boxes, command, *args):
    if command == 'delivery':
        for cupcake in args:
            boxes.append(cupcake)
    elif command == 'sell':
        if args:
            for cupcake in args:
                if type(cupcake) == int:
                    number_sold_cupcakes = int(cupcake)
                    for i in range(number_sold_cupcakes):
                        boxes.pop(0)
                else:
                    while cupcake in boxes:
                        boxes.remove(cupcake)
        else:
            boxes.pop(0)
    return boxes

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

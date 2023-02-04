from collections import deque


def stock_availability(list_of_flavours, command, *args):
    result = ''
    list_of_flavours = deque(list_of_flavours)
    if command == "delivery":
        list_of_flavours+=args
    else:
        if not args:
            list_of_flavours.popleft()
        else:
            for arg in args:
                if type(arg)==int:
                    for i in range(args[0]):
                        list_of_flavours.popleft()

                else:
                    while arg in list_of_flavours:
                        list_of_flavours.remove(arg)


    result = [*list_of_flavours]

    return result


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

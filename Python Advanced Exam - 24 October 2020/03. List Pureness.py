def numbers_searching(*args):
    result = []
    missing_num = None
    dublicates = set()
    min_num = min(args)
    max_num = max(args)

    for num in range(min_num, max_num+1):
        if args.count(num) == 0:
            missing_num = num
        elif args.count(num) > 1:
            dublicates.add(num)

    result.append(missing_num)
    list_of_dublicates = list(sorted(dublicates))

    result.append(list_of_dublicates)
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 44, 47, 45, 44, 44, 48, 44, 48))
print(numbers_searching(1, 2, 3, 4, 2, 5, 4))
print(numbers_searching(1, 2, 4, 5))
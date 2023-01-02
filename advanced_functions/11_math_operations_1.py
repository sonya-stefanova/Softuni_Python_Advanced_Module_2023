def is_valid_index(args, tuple):
    return 0 <= args < len(tuple)


def math_operations(*args, **kwargs):
    idx = 0
    zero_devision_error = False
    while True:

        if is_valid_index(idx, args):
            curr_num = args[idx]
            if idx % len(kwargs) == 0:
                kwargs["a"] += curr_num
                idx += 1

            elif idx % len(kwargs) == 1:
                kwargs["s"] -= curr_num
                idx += 1

            elif idx % len(kwargs) == 2:
                if curr_num == 0:
                    idx += 1
                    zero_devision_error = True
                    continue
                kwargs["d"] /= curr_num
                idx += 1

            elif idx % len(kwargs) == 3:
                kwargs["m"] *= args[idx]
                idx += 1
        else:
            break

    sorted_result = [f"{k}: {v:.1f}" for k,v in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))]
    return '\n'.join(sorted_result)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))

expression = input()

opening_brackets = []

balanced_parentheses = True

for symbol in expression:

    if symbol in '({[':
        opening_brackets.append(symbol)

    elif not opening_brackets:
        balanced_parentheses = False
        break

    else:
        last_opening_bracket = opening_brackets.pop()
        if f'{last_opening_bracket}{symbol}' not in '(){}[]':
            balanced_parentheses = False
            break

if balanced_parentheses and not opening_brackets:
    print('YES')
else:
    print('NO')

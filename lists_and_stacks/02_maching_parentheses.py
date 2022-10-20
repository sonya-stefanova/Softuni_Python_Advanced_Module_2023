
"""
To do:
 = > read the expression
 = > create empty stack to save the brackets 
 = > *loop* through the expression to check if there is an opening/closing bracket and push the opening index of
  the opening bracket into the stack. 
  When you meet a closing bracket check the index and pop the last opening bracket of the stack
 = > The sought expression is between the starting index and the end index
 => check if the expession is valid by using a counter for the brackets.
"""

# expression = "1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5"
# expression1 = "(2 + 3) - (2 + 3)"

expression = input()

s = []
for i in range(len(expression)):
    currrent_symbol = expression[i]
    if currrent_symbol == '(':
        s.append(i)
    elif currrent_symbol == ')':
        start_index = s.pop()
        end_index = i
        print(expression[start_index:end_index+1])

counter = 0
for each_char in expression:
    if each_char == '(':
        counter += 1
    elif each_char == ')':
        counter -= 1
# print(counter)

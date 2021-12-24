# Перевод префиксной нотации в инфиксную.

from collections import deque

def prefixTOinfix (expr):
    operators = {'+','-','*','/'}
    expr = expr.split(" ")
    stack = deque()
    
    for i in range(len(expr)-1, -1, -1):
        symbol = expr[i]
        if symbol in operators:
            subexpr = f"({stack.pop()} {symbol} {stack.pop()})"
            stack.append(subexpr)
        else:
            stack.append(symbol)
            
    return stack.pop()        

prefix = "/ + 3 10 * + 2 3 - 3 5"
infix = prefixTOinfix (prefix)

print(infix)
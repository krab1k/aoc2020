import string

def e(op, s, arg):
    if op == '+':
        s += arg
    else:
        s *= arg
    return s


def evaluate_expression(expr):
    s = None
    op = None
    arg = None

    length = len(expr)
    i = 0
    while i < length:
        c = expr[i]
        i += 1
        if c == ' ':
            continue
        if c == '+':
            op = '+'
        if c == '*':
            op = '*'
            return s * evaluate_expression(expr[i:])
        if c.isdigit():
            arg = int(c)
            if op is not None:
                s = e(op, s, arg)
        if c == '(':
            j = i 
            p = 1
            while p != 0:
                if expr[j] == '(':
                    p += 1
                elif expr[j] == ')':
                    p -= 1
                j += 1
            arg = evaluate_expression(expr[i:j -1])
            i = j + 1
            if op is not None:
                s = e(op, s, arg)
        if s is None:
            s = arg
    
    return s



def main():
    expressions = []
    with open('input.txt') as f:
        for line in f:
            expressions.append(line.strip())
    s = 0
    for expr in expressions:
        x = evaluate_expression(expr)
        s += x

    print(s)


if __name__ == '__main__':
    main()

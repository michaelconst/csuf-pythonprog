from mod1.homework.utils.stack import Stack
from keyword import iskeyword

from mod1.homework.evaluate_postfix import postfix_eval


def infix2postfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token.isidentifier() and not iskeyword(token) or token.isnumeric():
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        elif token in prec:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


print(infix2postfix("A * B + C * D"))
print(infix2postfix("( A + B ) * C - ( D - E ) * ( F + G )"))

print(postfix_eval(infix2postfix("3 + 4 * ( 7 - 3 ) / 4")))

'''
author: mconstantin
'''


from keyword import iskeyword
from abc import abstractmethod, ABC
import math
from mod1.homework.utils.stack import Stack


OPERATOR_PLUS = '+'
OPERATOR_MINUS = '-'
OPERATOR_MUL = '*'
OPERATOR_DIV = '/'
OPERATOR_SQRT = 'sqrt'


class Operator:
    @classmethod
    def fromsymbol(cls, symbol):
        for clazz in cls.__subclasses__():
            if symbol == getattr(clazz, 'symbol'):
                return clazz()

    @classmethod
    def get_symbols(cls):
        return [clazz.symbol for clazz in cls.__subclasses__() if hasattr(clazz, 'symbol')]

    @classmethod
    def is_operator(cls, symbol):
        return symbol in cls.get_symbols()

    def __eq__(self, other):
        cls = self.__class__
        other_cls = other.__class__
        if cls.__name__ == other_cls.__name__:
            return True
        return hasattr(cls, 'priority') and hasattr(other_cls, 'priority') and cls.priority == other_cls.priority

    def __gt__(self, other):
        cls = self.__class__
        other_cls = other.__class__
        try:
            return cls.priority > other_cls.priority
        except AttributeError as e:
            raise TypeError(str(e))

    def __lt__(self, other):
        cls = self.__class__
        other_cls = other.__class__
        try:
            return cls.priority < other_cls.priority
        except AttributeError as e:
            raise TypeError(str(e))

    def __ge__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return not self.__gt__(other)

    def __str__(self):
        return self.__class__.symbol


class Plus(Operator):
    symbol = OPERATOR_PLUS
    priority = 2


class Minus(Operator):
    symbol = OPERATOR_MINUS
    priority = 2


class Multiply(Operator):
    symbol = OPERATOR_MUL
    priority = 3


class Divide(Operator):
    symbol = OPERATOR_DIV
    priority = 3


class Sqrt(Operator):
    symbol = OPERATOR_SQRT
    priority = 4


class Calculator:
    @classmethod
    def infix2postfix(cls, infix_expr):
        op_stack = Stack()
        postfix_list = []
        token_list = infix_expr.split()

        for token in token_list:
            if token in Operator.get_symbols():
                while not op_stack.isEmpty():
                    top_of_stack = op_stack.peek()
                    op1 = Operator.fromsymbol(top_of_stack)
                    op2 = Operator.fromsymbol(token)
                    if op1 is None:
                        break
                    if op1 >= op2:
                        postfix_list.append(op_stack.pop())
                    else:
                        break
                op_stack.push(token)
            elif token.isidentifier() and not iskeyword(token) or token.isnumeric():
                postfix_list.append(token)
            elif token == '(':
                op_stack.push(token)
            elif token == ')':
                top_token = op_stack.pop()
                while top_token != '(':
                    postfix_list.append(top_token)
                    top_token = op_stack.pop()
            else:
                raise ValueError('token \'{}\' is not valid'.format(token))
            print('token={}, postfix={}, stack.py={}'.format(token, str(postfix_list), str(op_stack)))

        while not op_stack.isEmpty():
            postfix_list.append(op_stack.pop())
        return " ".join(postfix_list)

    @classmethod
    def _build_tree(cls, postfix_expr):
        expr_stack = Stack()
        token_list = postfix_expr.split()

        for token in token_list:
            if token in Operator.get_symbols():
                if Expression._is_binary(token):
                    right_expr = expr_stack.pop()
                    left_expr = expr_stack.pop()
                    expr = BinaryExpression.create(token, left_expr, right_expr)
                    expr_stack.push(expr)
                else:
                    # unary operator
                    operand = expr_stack.pop()
                    expr = UnaryExpression.create(token, operand)
                    expr_stack.push(expr)
            else:
                expr_stack.push(TerminalExpression(token))

        return expr_stack.pop()

    @classmethod
    def build_expr(cls, infix_expr):
        return cls._build_tree(cls.infix2postfix(infix_expr))

    @classmethod
    def postfix_eval(cls, postfix_expr, context=None):
        expr_tree = cls._build_tree(postfix_expr)
        return expr_tree.evaluate(context=context)

    @staticmethod
    def calculate(infix_expr):
        return Calculator.postfix_eval(Calculator.infix2postfix(infix_expr))


class Context:
    def __init__(self, d):
        try:
            self.__variables = dict(d)
        except TypeError:
            raise ValueError('cannot create context with this value {!r}'.format(d))

    def add_var(self, name, value):
        if not iskeyword(name):
            raise ValueError('{} is not a valid variable name'.format(name))
        try:
            self.__variables[name] = int(value)
        except ValueError as e:
            raise ValueError('{} is not an integer value'.format(value))
        except TypeError as e:
            raise ValueError('{} is not a valid variable name'.format(name))

    def get_var(self, name):
        try:
            return int(self.__variables[name])
        except ValueError:
            raise ValueError('{} is not an integer value'.format(name))
        except KeyError:
            raise ValueError('{} is not found'.format(name))


class Expression(ABC):
    @staticmethod
    def _is_binary(op):
        for bin_expr_type in Expression._get_all_subclasses(BinaryExpression):
            if bin_expr_type.op == op:
                return True
        return False

    @staticmethod
    def _get_all_subclasses(cls):
        """ Recursively generate of all the subclasses of class cls. """
        for subclass in cls.__subclasses__():
            yield subclass
            for subclass in Expression._get_all_subclasses(subclass):
                yield subclass

    @abstractmethod
    def evaluate(self, context=None):
        '''return the value of the expression'''


class BinaryExpression(Expression):
    @classmethod
    def create(cls, op, left_expr, right_expr):
        for subclass in Expression._get_all_subclasses(cls):
            if subclass.op == op:
                return subclass(left_expr, right_expr)
        else:  # no subclass with matching op found
            raise ValueError('operator "{}" has no corresponding binary operation'.format(op))

    def __init__(self, op, left_expr, right_expr):
        if not isinstance(left_expr, Expression) or not isinstance(right_expr, Expression):
            raise TypeError('left or right operands are not an Expression')
        self.__left = left_expr
        self.__right = right_expr

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    def __iter__(self):
        return (e for e in (self.left, self.right))

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right and self.op == other.op

    def __str__(self):
        left_str = str(self.left)
        right_str = str(self.right)
        if isinstance(self.left, BinaryExpression) and Operator.fromsymbol(self.left.op) < Operator.fromsymbol(self.op):
            left_str = '( ' + left_str + ' )'
        if isinstance(self.right, BinaryExpression) and Operator.fromsymbol(self.right.op) < Operator.fromsymbol(self.op):
            right_str = '( ' + right_str + ' )'
        return left_str + ' ' + self.op + ' ' + right_str

    def __repr__(self):
        cls_name = type(self).__name__
        return '{} ({!r} {} {!r})'.format(cls_name, self.left, self.op, self.right)

    def __format__(self, format_spec):
        if format_spec.endswith('p'):
            return '{} {} {}'.format(format(self.left, format_spec), format(self.right, format_spec), self.op)
        else:
            left_fmt = '{}'
            right_fmt = '{}'
            if isinstance(self.left, BinaryExpression) and Operator.fromsymbol(self.left.op) < Operator.fromsymbol(self.op):
                left_fmt = '( {} )'
            if isinstance(self.right, BinaryExpression) and Operator.fromsymbol(self.right.op) < Operator.fromsymbol(self.op):
                right_fmt = '( {} )'
            return (left_fmt + ' {} ' + right_fmt).format(format(self.left, format_spec), self.op,
                                                        format(self.right, format_spec))

    def __hash__(self):
        return hash(self.left) ^ hash(self.op) ^ hash(self.right)


class TerminalExpression(Expression):
    def __init__(self, token):
        self.__token = token

    @property
    def token(self):
        try:
            return float(self.__token)
        except ValueError:
            return self.__token

    def evaluate(self, context=None):
        try:
            return float(self.token)
        except ValueError:
            if context:
                return context.get_var(self.__token)

    def __str__(self):
        return self.__token

    def __repr__(self):
        cls_name = type(self).__name__
        return '{} {!r}'.format(cls_name, self.__token)

    def __format__(self, format_spec):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
        return format(self.token, format_spec)

    def __hash__(self):
        return hash(self.token)


class AddExpression(BinaryExpression):
    op = OPERATOR_PLUS

    def __init__(self, left_expr, right_expr):
        super().__init__(None, left_expr, right_expr)

    def evaluate(self, context=None):
        return self.left.evaluate(context=context) + self.right.evaluate(context=context)


class SubtractExpression(BinaryExpression):
    op = OPERATOR_MINUS

    def __init__(self, left_expr, right_expr):
        super().__init__(None, left_expr, right_expr)

    def evaluate(self, context=None):
        return self.left.evaluate(context=context) - self.right.evaluate(context=context)


class MultiplyExpression(BinaryExpression):
    op = OPERATOR_MUL

    def __init__(self, left_expr, right_expr):
        super().__init__(None, left_expr, right_expr)

    def evaluate(self, context=None):
        return self.left.evaluate(context=context) * self.right.evaluate(context=context)


class DivideExpression(BinaryExpression):
    op = OPERATOR_DIV

    def __init__(self, left_expr, right_expr):
        super().__init__(None, left_expr, right_expr)

    def evaluate(self, context=None):
        return float(self.left.evaluate(context=context)) / self.right.evaluate(context=context)


class UnaryExpression(Expression):
    def __init__(self, operand):
        self.__operand = operand

    @property
    def operand(self):
        return self.__operand

    @classmethod
    def create(cls, op, expr):
        for subclass in Expression._get_all_subclasses(cls):
            if subclass.op == op:
                return subclass(expr)
        else:  # no subclass with matching op found
            raise ValueError('operator "{}" has no corresponding unary operation'.format(op))

    def __str__(self):
        return self.op + ' ( ' + str(self.operand) + ' )'

    def __repr__(self):
        cls_name = type(self).__name__
        return '{} {!r}'.format(cls_name, self.operand)

    def __format__(self, format_spec):
        if format_spec.endswith('p'):
            return '{} {}'.format(format(self.operand, format_spec), self.op)
        else:
            return '{} {}'.format(self.op, format(self.operand, format_spec))

    def __hash__(self):
        return hash(self.operand) ^ hash(self.op)


class SquareRoot(UnaryExpression):
    op = OPERATOR_SQRT

    def evaluate(self, context=None):
        return math.sqrt(self.operand.evaluate(context))


if __name__ == '__main__':
    infix_expr = "3 + sqrt 4 * ( 7 - 3 ) / 4"
    expr = Calculator.build_expr(infix_expr)

    infix_expr = "8 / ( 5 - 3 )"
    expr = Calculator.build_expr(infix_expr)

    # supported by __str__ method
    print('str: ' + str(expr))
    # supported by __repr__ method
    print('repr: ' + repr(expr))
    # supported by __format__ method
    print('format postfix: ' + format(expr, 'p'))
    print('format infix float: ' + format(expr, '0.1f'))
    # supported by __iter__ method
    l, r = expr
    print('left: ' + str(l))
    print('right: ' + str(r))
    # supported by __hash__ method
    s = set(expr)
    print('hash: ' + str(hash(expr)))

    print(Calculator.calculate(infix_expr))

from compiler import Compiler
import ox
import re
import inspect #inspect.getsource

from sidekick.placeholder import *

class JsCompiler(Compiler):

    """
    Javascript compiler.
    """

def compile(ql, **kwargs):
    """
    Compiles quick lambda object to Javascript.
    """

    _input = str('ql')

    parse(_input)
    compiler = JsCompiler(ql)
    return compiler.compile(**kwargs)

class Ast(opt.BinOp(callable, object, object)
          | opt.SingleOp(callable, object)
          | opt.Call(object, tuple, dict)
          | opt.GetAttr(object, str)
          | opt.Placeholder(int)
          | opt.Cte(object)):
    """
    AST node for a placeholder expression.
    """



tokens = [
    'OP',
    'BREAKLINE',
    'ATRIB_OP',
    'BOOLEAN',
    'STRINGS',
    'NUMBER',
]

# Quick lambdas

# >>> inc = fn(_ + 1)
# >>> total_cost = fn(_.num_items * _.price)

'''
    A Parser to emit js code from python
'''

# Parser Operations

def js_parser(tokens):
    parser = ox.make_parser([
        ('term : term OP atom', binary_operator),
        ('term : atom', lambda x: x),
        ('atom : BREAKLINE', lambda x: x),
        ('atom : BOOLEAN', parse_booleans),
        ('atom : ATRIB_OP', lambda x: x),
        ('atom : STRINGS', lambda x: str(x)),
        ('atom : NUMBER', lambda x: float(x))
    ], tokens)

    return parser



def parse_booleans(binary):
    if binary:
        binary = 'true'
    else:
        binary = 'false'

    return binary


def parse_operations(first_value, second_value, operator):

    if operator is '+' or operator is '-' or operator is '*' or operator is '/':
        return binary_operator(first_value, operator, second_value)

# Binary Operator

OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

def binary_operator (first_value, operator, second_value):
    return Ast.BinOp(OPERATORS[operator],  first_value, second_value)

# Backlog

def parse_expressions(statements):
    return "Some expression in JS"

# Evaluate

def evaluate(tree):
    return 'a'

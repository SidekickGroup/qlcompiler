from compiler import Compiler
from sidekick import _
import operator as op
import ipdb

globals = {
    op.add: lambda x, y: '{} + {}'.format(x, y),
    op.sub: lambda x, y: '{} - {}'.format(x, y),
    op.mul: lambda x, y: '{} * {}'.format(x, y),
    op.truediv: lambda x, y: '{} / {}'.format(x, y),
    op.lt: lambda x, y: '{} < {}'.format(x, y),
    op.le: lambda x, y: '{} <= {}'.format(x, y),
    op.eq: lambda x, y: '{} == {}'.format(x, y),
    op.ne: lambda x, y: '{} != {}'.format(x, y),
    op.gt: lambda x, y: '{} > {}'.format(x, y),
    op.ge: lambda x, y: '{} >= {}'.format(x, y),
    op.mod: lambda x, y: '{} % {}'.format(x, y),
    op.pow: lambda x, y: '{} ** {}'.format(x, y),
    op.invert: lambda x: '~{}'.format(x),
    op.neg: lambda x: '-{}'.format(x),
    op.pos: lambda x: '+{}'.format(x),
    
}

consts = {}

python_fn = {
    'abs',
    'cmp',
    'len',
    'list',
    'map',
    'min',
    'print',
    'str',
    'pow',
    'ord',
    'filter',
    'enumerate',
    'eval',
    'getattr',
    'hex',
    'float',
    'dict',
    'chr',
    'type',
    'hash',
}


class JsCompiler(Compiler):

    """
    Javascript compiler.
    """

def compile(ql, **kwargs):
    """
    Compiles quick lambda object to Javascript.
    """
    # ipdb.set_trace()
    types = ['binop', 'singleop', 'call', 'getattr', 'placeholder', 'cte']
    example = _ + 2
    
    if type(ql) is (type(int()) or type(float())):
      _type = 'cte'
    elif type(ql) is not type(example):
        raise Exception("The object isn't a sidekick placeholder (quick lambda)!")
    else:
        command = 'ql._ast.'
        _type = None
        for t in types:
            if eval(command + t):
                _type = t
                break

        if not _type:
            raise Exception("Didn't find the quick lambda type for the object '%s'" % ql)

        command = 'ql._ast.' + _type + '_args'
        args = eval(command)

    if _type is 'binop':
        func = globals[args[0]](args[1], args[2])

    elif _type is 'singleop':
        func = globals[args[0]](args[1])

    elif _type is 'call':
        func = ''

    elif _type is 'getattr':
        x = str(args[0])
        y = str(args[1])
        func = y + '.' + x

    elif _type is 'placeholder':
        func = '_'

    elif _type is 'cte':
        func = str(float(ql))

    return func
    #return compiler.compile(**kwargs)



# class Ast(opt.BinOp(callable, object, object)
#           | opt.SingleOp(callable, object)
#           | opt.Call(object, tuple, dict)
#           | opt.GetAttr(object, str)
#           | opt.Placeholder(int)
#           | opt.Cte(object)):
#     """
#     AST node for a placeholder expression.
#     """

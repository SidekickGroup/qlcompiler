from compiler import Compiler
from sidekick import _
import operator as op

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
}

class JsCompiler(Compiler):

    """
    Javascript compiler.
    """

def compile(ql, **kwargs):
    """
    Compiles quick lambda object to Javascript.
    """
    types = ['binop', 'singleop', 'call', 'getattr', 'placeholder', 'cte']
    example = _ + 2
    if type(ql) is not type(example):
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
        print(func)

    return args
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

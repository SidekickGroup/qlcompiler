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
    'len',
    'map',
    'min',
    'print',
    'str',
    'pow',
    'ord',
    'filter',
    'enumerate',
    'eval',
    'hex',
    'float',
    'chr',
    'type',
}

js_fn = {
    'abs': lambda ql: 'Math.abs({})'.format(ql),
    'len': lambda ql: '{}.length'.format(ql),
    'map': lambda array,function: '{}.map({})'.format(array, function),
    'min': lambda x, y: 'Math.min({}, {})'.format(x,y),
    'print': lambda ql: 'console.log({})'.format(ql),
    'str': lambda ql: 'String({})'.format(ql),
    'ord': lambda ql: '{}.charCodeAt()'.format(ql),
    'filter': lambda array,function: '{}.filter({})'.format(array, function),
    'enumerate': lambda array: '{}.entries()'.format(array),
    'eval': lambda string: 'eval({})'.format(string),
    'hex': lambda ql: '{}.toString(16)'.format(ql),
    'float':lambda ql: 'parseFloat({})'.format(ql),
    'chr': lambda ql: 'String.fromCharCode({})'.format(ql),
    'type': lambda ql: 'typeof({})'.format(ql),
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

        print(args[0])
        print(args[1])
        print(args[1][1])
        print(args[1][1])

        func =  js_fn['abs'](args[0])

    elif _type is 'getattr':
        x = str(args[0])
        y = str(args[1])
        func = '{}.getAttribute("{}")'.format(y, x)

    elif _type is 'placeholder':
        func = '_'

    elif _type is 'cte':
        func = str(float(ql))

    return func
    #return compiler.compile(**kwargs)

def call_js_fn():

    return 10



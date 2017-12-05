from qlcompiler.compiler import Compiler


class CCompiler(Compiler):
    """
    C compiler.
    """


def compile(ql, **kwargs):
    """
    Compiles quick lambda object to C.
    """

    return Compiler.compile(**kwargs)

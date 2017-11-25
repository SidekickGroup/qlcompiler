import re
import click
import ox

from js_parser import JsParser

class JsEvaluater():

    """
        Evaluate an AST to provide an output
    """


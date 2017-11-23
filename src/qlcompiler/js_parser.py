 import ox

class JSParser():


    # Quick lambdas
    # >>> inc = fn(_ + 1)
    # >>> total_cost = fn(_.num_items * _.price)

    '''
       A Parser to emit js code from python 
    '''

    def js_parser(tokens):
        parser = ox.make_parser([
            ('term : term OP atom', binary_operator),
            ('term : atom', lambda x: x), 
            ('atom: BREAKLINE', lambda x: x),
            ('atom: ATRIB_OP', lambda x: x),
            ('atom: BOOLEAN', parse_booleans), 
            ('atom: STRINGS', lambda x: str(x)), 
            ('atom: NUMBER', lambda x: float(x))
        ], tokens)
        
        return parser

    # Parser Operations

    def parse_booleans(binary): 
        if binary:
            binary = 'true'
        else:
            binary = 'false'
    
        return binary


    def parse_operations(first_value, second_value, operator):

        if operator == '+' || operator == '-' || operator == '*' || operator == '/':
            return binary_operator(first_value, operator, second_value)            
 
    # Binary Operator

    OPERATORS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

    def binary_operator (first_value, second_value, operator):
        return OPERATORS[operator](first_value, second_value)
   
    # Backlog

    def parse_expressions(statements):
        return "Some expression in JS"

    # Evaluate

    def evaluate(tree): 

   
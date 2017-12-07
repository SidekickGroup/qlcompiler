class Compiler:
    """
    Base compiler class.
    """

    def __init__(self, function):
        self.function = function

    def compile(self):
        """
        Compile function emiting code to the target language.
        """

        js_frame = '''
        function (_) { 
            return %s; 
        }'''

        if self['language'] == 'JS':
            if self['type'] != 'call':
                return js_frame % self['function']
            else:
                js_frame = '''
                function () { 
                    %s 
                    return _; 
                }'''
                return js_frame % self['function']
        else:
            raise NotImplementedError
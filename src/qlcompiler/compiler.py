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
        }
        '''

        if self['language'] == 'JS':
            return js_frame % self['function']
        else:
            raise NotImplementedError
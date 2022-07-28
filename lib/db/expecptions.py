class ValidationError(Exception):
    def __init__(self,errors):
        self.errors = errors

    def __str__(self):
        value = ''
        if type(self.errors) == dict:
            for field in self.errors.values():
                for error in field:
                    value+=f' * {error} \n'
        elif type(self.errors) == list:
            for v in self.errors:
                value+=f' * {v} \n'
        else:
            value = str(self.errors)
        return value

    def __repr__(self):
        return str(self.errors)
    
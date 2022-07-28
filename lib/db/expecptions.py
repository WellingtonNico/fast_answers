class ValidationError(Exception):
    def __init__(self,errors):
        self.errors = errors
    def __str__(self):
        return str(self.errors)
    def __repr__(self):
        return str(self.errors)
    
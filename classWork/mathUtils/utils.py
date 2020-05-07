
class MathUtilsException (Exception):
    def __init__(self, message):
        if message:
            self.message = message
        else:
            self.message = 'MathError!'
    
    def __str__(self):
        return self.message


def sum(a, b):
    return a + b

def multiply(a, b):
    return a * b

def difference(a, b):
    return a - b

def divide(a, b):
    if b == 0: 
        raise MathUtilsException('DIVISION BY 0!!')
    return a/b

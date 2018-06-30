# class MyError is derived from super class Exception
class ClassNotFound(Exception):

    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        s = 'Class name not found or new class name for these field {}'
        return repr(s.format(self.value))



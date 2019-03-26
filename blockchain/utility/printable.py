"""This is a base class and has a __repr__() which returns string objects. The __repr__() here is used to
return the object of the class as a dictionary using __dict__() function. The dictionary is then converted 
to a string and is returned by __repr__(). """

class Printable:
    """A base class which implements printing functionality."""
    def __repr__(self):
        return str(self.__dict__)

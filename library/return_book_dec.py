import os
from datetime import date

def dekorator(func):
    """
    Decorator function to handle book returning operations.

    args:
        func (function): Function to be decorated.

    returns:
        function: Wrapper function.
    """
    def wrapper(customer_id, *args):
        for book in args:
            func(customer_id, book)
    return wrapper
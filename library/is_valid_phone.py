import pandas as pd


def phone_val(number: str) -> bool:
    """
    Checks if the phone number is 9-digit long.

    args:
        number (str): The phone number to be validated.

    returns:
        bool: True if the phone number is valid, False otherwise.
    """
    if len(number) != 9:
        return False
    else:
        return True

"""
NAME
    loan_book.py

DESCRIPTION
    This module provides functions to handle book borrowing and returning operations
    for customers in the library system.

    This script requires os, pandas, datetime, and return_book_dec modules to be installed within
    the Python environment you are running this script in.

FUNCTIONS
    This module contains the following functions:
    - borrow_books(customer_id, *args):
        Allows a customer to borrow books from the library.
            returns True if the books are borrowed successfully, False otherwise.

    - return_book(customer_id, book):
        Allows a customer to return a borrowed book to the library.
            returns True if the book is returned successfully, False otherwise.

EXAMPLES
    - borrow_books(5488, "Quo Vadis", "Pan Tadeusz")
    - return_book(5488, "Quo Vadis")
"""
import os
import pandas as pd
from datetime import date
from return_book_dec import dekorator
def borrow_books(customer_id, *args):
    """
    Allows a customer to borrow books from the library.

    Args:
        customer_id (int): The ID of the customer borrowing the books.
        *args (str): List of book titles to be borrowed.

    Returns:
        bool: True if books are borrowed successfully, False otherwise.
    """
    df=pd.read_csv('database/book.csv')
    if os.path.exists("dataset"):
        with open(f"dataset/{customer_id}.txt", "a")as file:
            for title in args:

                book=df[df['TITLE'] == title].index.values[0]
                book=df.loc[book]
                print(book)
                print(book['AUTHOR'])
                print(book['TITLE'])
                print(book['PAGES'])
                file.write(f"Author:{book['AUTHOR']},Title:{book['TITLE']},Pages:{book['PAGES']},Borrowed:{date.today()},returned=False \n")
        return True
    else:
        print("Nieprawidlowe dane")
        return False
@dekorator
def return_book(customer_id, book):
    """
    Allows a customer to return a borrowed book to the library.

    Args:
        customer_id (int): The ID of the customer returning the book.
        book (str): Title of the book to be returned.

    Returns:
        bool: True if the book is returned successfully, False otherwise.
        """
    if os.path.exists(f"dataset/{customer_id}.txt"):
        with open(f"dataset/{customer_id}.txt", "r") as file:
            lines=file.readlines()
            for i,line in enumerate(lines):
                if book in line:
                    lines[i]=line.replace("False",f"{date.today()}")
        with open(f"dataset/{customer_id}.txt", "w") as file:
            file.writelines(lines)
        return True
    else:
        print("Ksiażka nie zostala wyporzyczona")
        return False

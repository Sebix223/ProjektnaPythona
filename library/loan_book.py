import os
import pandas as pd
from datetime import date
def borrow_books(customer_id, *args):
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

    else:
        print("Nieprawidlowe dane")


def return_book(customer_id, book):
    if os.path.exists(f"dataset/{customer_id}.txt"):
        with open(f"dataset/{customer_id}.txt", "r") as file:
            lines=file.readlines()
            for i,line in enumerate(lines):
                if book in line:
                    lines[i]=line.replace("False",f"{date.today()}")
        with open(f"dataset/{customer_id}.txt", "w") as file:
            file.writelines(lines)
    else:
        print("Ksiażka nie zostala wyporzyczona")

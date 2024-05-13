import csv
import pandas as pd
from datetime import date

def Add_book(title, author, pages ):

    df = pd.read_csv('database/book.csv', index_col="ID")
    book_index = df.index.max()
    time = date.today()
    df.loc[book_index + 1] = [author, title, pages, time, time]
    df.to_csv("database/book.csv")
def delete_book( ID=None,title=None):
    try:
        df = pd.read_csv("database/book.csv")
        if ID is not None:
            if ID not in df['ID'].values:
                raise ValueError(f"ksiązka o ID {ID} nie istnieje w bazie danych. spróbuj ponownie.")
            df = df[df['ID'] != ID]
        elif title is not None:
            if title not in df['TITLE'].values:
                raise ValueError(f"Książka o tytule {title} nie istnieje w bazie danych.")
            df = df[df['TITLE'] != title]
        else:
            print("Ksiązka zostala usunieta")
        df.to_csv("database/book.csv",index=False)
    except FileNotFoundError:
        print("plik bazy danych nie zostal odnaleziony")
    except ValueError as e:
        print(e)

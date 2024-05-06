import csv
import pandas as pd
from datetime import date

def Add_book(title, author, pages ):
    df = pd.read_csv('database/book.csv',index_col="ID")
    book_index=df.index.max()
    time = date.today()
    df.loc[book_index+1]=[author,title,pages,time,time]
    df.to_csv("database/book.csv")
def delete_book( ID=None,title=None):
    df = pd.read_csv("database/book.csv")
    if ID is not None:
        df = df[df['ID'] != ID]
    elif title is not None:
        df = df[df['TITLE'] != title]
    df.to_csv("database/book.csv",index=False)
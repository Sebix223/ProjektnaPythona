import pandas as pd
import os
import random
from datetime import date

database='DATABASE'

def generuj_id_klienta():


    ID_number=random.randint(1000, 9999)
    try:
        df_customer = pd.read_csv("database/customer.csv")
    except FileNotFoundError as e:
        print(e)
        return False
    while ID_number in df_customer["ID"].values:
        ID_number = random.randint(1000, 9999)
    return ID_number

def rejestracja_klienta():
    id_klienta = generuj_id_klienta()
    if not os.path.exists("dataset"):
        os.mkdir("dataset")
    with open(os.path.join("dataset", f"{id_klienta}.txt"), "w") as file:
        pass
    return id_klienta

def dodaj_dane_klienta( imie, nazwisko, mail, phone,street, city,country):

    id_klienta = rejestracja_klienta()
    df_customer = pd.read_csv("database/customer.csv", index_col="ID")
    df_address = pd.read_csv('database/address.csv', index_col="ID")
    time=date.today()
    df_customer.loc[id_klienta] = [f"{imie} {nazwisko}", mail, phone, time, time]
    df_address.loc[id_klienta] = [street, city,country]


    df_customer.to_csv("database/customer.csv")
    df_address.to_csv('database/address.csv')

    return id_klienta



def usun_dane_klienta(ID=None, imie=None):
    try:
        df_customer = pd.read_csv('database/customer.csv')
        df_address = pd.read_csv('database/address.csv')

        if ID is not None:
            if ID not in df_customer['ID'].values:
                raise ValueError(f"Klient o ID {ID} nie istnieje w bazie danych.  Spróbuj ponownie.")
            df_customer = df_customer[df_customer['ID'] != ID]
            df_address = df_address[df_address['ID'] != ID]
        elif imie is not None:
            if imie not in df_customer['NAME'].values:
                raise ValueError(f"Nie znaleziono klienta o imienu {imie}.  Spróbuj ponownie.")
            customer_ID = df_customer[df_customer['NAME'==imie]].ID.values[0]
            df_customer = df_customer[df_customer['NAME'] != imie]
            df_address = df_address[df_address['ID']!=customer_ID]

        df_customer.to_csv('database/customer.csv', index=False)
        df_address.to_csv('database/address.csv', index=False)
        print("Dane klienta zostały usunięte pomyślnie.")
    except FileNotFoundError:
        print('Plik bazy danych nie zostal odnaleziony.')
    except ValueError as e:
        print(e)




import pandas as pd
import os
import random
from datetime import date
database='DATABASE'

def generuj_id_klienta():
    number=random.randint(1000, 9999)
    df_customer = pd.read_csv("database/customer.csv")
    while number in df_customer["ID"].values:
        number = random.randint(1000, 9999)
    return number

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
    df_address = pd.read_csv('database/address.csv',index_col="ID")

    time=date.today()
    df_customer.loc[id_klienta] = [f"{imie} {nazwisko}", mail, phone, time, time]
    df_address.loc[id_klienta] = [street, city,country]


    df_customer.to_csv("database/customer.csv")
    df_address.to_csv('database/address.csv')

    return id_klienta

def usun_dane_klienta(ID=None, imie=None):
    df_customer = pd.read_csv('database/customer.csv')
    df_address = pd.read_csv('database/address.csv')

    if ID is not None:
        df_customer = df_customer[df_customer['ID'] != ID]
        df_address = df_address[df_address['ID'] != ID]
    elif imie is not None:
        customer_ID = df_customer[df_customer['NAME'==imie]].ID.values[0]
        df_customer = df_customer[df_customer['NAME'] != imie]
        df_address = df_address[df_address['ID']!=customer_ID]

    df_customer.to_csv('database/customer.csv', index=False)
    df_address.to_csv('database/address.csv', index=False)




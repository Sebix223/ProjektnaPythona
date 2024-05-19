import serviceuser
import servicbook
import loan_book
def main():
    while True:
        print("\nWitaj w bibliotece!\n")
        print("1. Dodaj nową książkę")
        print("2. Usuń książkę")
        print("3. Rejestracja nowego klienta")
        print("4. Usuń dane klienta")
        print("5. Wypożycz ksiazke")
        print("6. Zwróć ksiązke")
        print("0. Wyjdź z programu\n")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            tytul = input("Podaj tytuł książki: ")
            autor = input("Podaj autora książki: ")
            strony = int(input("Podaj strony"))
            servicbook.Add_book( tytul, autor, strony)


        elif choice == "2":
            usun_opcja = input("Usunąć książkę wg ID czy tytułu? (ID/TYTUŁ): ").upper()
            if usun_opcja == "ID":
                identyfikator = int(input("Podaj ID książki do usunięcia: "))
                servicbook.delete_book( ID=identyfikator)
            elif usun_opcja == "TYTUŁ":
                tytul = input("Podaj tytuł książki do usunięcia: ")
                servicbook.delete_book( title=tytul)
            else:
                print("Nieprawidłowa opcja.")

        elif choice == "3":
            imie = input("Podaj imię nowego klienta: ")
            nazwisko = input("Podaj nazwisko nowego klienta: ")
            while True:
                email = input("Podaj email nowego klienta:")
                if "@wp.pl" in email or "@gmail.pl" in email:
                    break
                else:
                    print("Email musi zawierać @wp.pl lub @gmail.pl. Spróbuj ponownie.")

            while True:
                numer = int(input("Podaj numer :"))
                if len(str(numer)) != 9:
                    print(f"podany {numer} sie nie zgadza. Sproboj ponownie")
                else:
                    break
            ulica = input("Podaj ulica:")
            miasto = input("Podaj miasto:")
            kraj = input("Podaj kraj:")

            id_klienta = serviceuser.dodaj_dane_klienta(imie, nazwisko, email, numer, ulica, miasto, kraj)
            print(f"Nowy klient został zarejestrowany. ID klienta: {id_klienta}")

        elif choice == "4":
            usun_opcja = input("Usunąć dane klienta wg ID czy imienia? (ID/IMIĘ): ").upper()

            if usun_opcja == "ID":
                identyfikator = int(input("Podaj ID klienta do usunięcia: "))
                serviceuser.usun_dane_klienta(ID=identyfikator)
            elif usun_opcja == "IMIĘ":
                imie = input("Podaj imię klienta do usunięcia: ")
                serviceuser.usun_dane_klienta(imie=imie)
            else:
                print("Nieprawidlowa opcja")
        elif choice == "5":
            id_klienta = int(input("Podaj id klienta:"))
            tytuly=[]
            while True:
                tytul=input("zeby przerwac dzialanie podaj 0 lub 100")
                if tytul == "0" or tytul == "100":
                    break
                tytuly.append(tytul)
            loan_book.borrow_books(id_klienta,*tytuly)




        elif choice == "6":
             id_klienta = int(input("Podaj ID klienta:"))
             tytul_ksiazki = input("Podaj tytul ksiązki:")
             loan_book.return_book(id_klienta,tytul_ksiazki)
             print("Ksiązka oddana pomyslnie")
        elif choice == "0":
            print("do widzenia")
            break
        else:
            print("nieprawidlowa Opcja.")


if __name__ == "__main__":
    main()





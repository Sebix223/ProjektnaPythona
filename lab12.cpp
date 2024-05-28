#include <iostream>
#include <string>
#include <vector>
#include <time.h>



using namespace std;

class Osoba {
private:
    string imie;
    int rokUrodzenia;

public:
    Osoba(){}
    Osoba(string imie, int rokUrodzenia):imie(imie),rokUrodzenia(rokUrodzenia){}

    string toString() {
        return "Imie: " + imie + ", Rok urodzenia: " + to_string(rokUrodzenia);
    }

    int getRokUrodzenia() {
        return rokUrodzenia;
    }
    int wiek()
    {
        int rok_teraz=2024;
        return rok_teraz-rokUrodzenia;
    }
    int getwiek()
    {
        return rokUrodzenia;
    }
    string getimie()
    {
        return imie;
    }
};
class Pracownik:public Osoba
{
protected:
    double pensja;
public:
    Pracownik(){}
    Pracownik(string imie, int rokUrodzenia,double pensja):Osoba(imie, rokUrodzenia),pensja(pensja){}


};
class Student:public Osoba
{
protected:
    double srednia;
public:
    Student(){}
    Student(string imie, int rokUrodzenia,double srednia):Osoba(imie, rokUrodzenia),srednia(srednia){}

};
class Kierownik:public Pracownik
{
protected:
    string stanowisko;
public:
    Kierownik(){}
    Kierownik(string imie,int rokUrodzenia,double pensja,string stanowisko):Pracownik(imie,rokUrodzenia, pensja),stanowisko(stanowisko){}
};
int main(){
    Osoba *o1 = new Osoba("Ala", 2009);
    Osoba *o2 = new Pracownik("Ewa", 1995, 3456.67);
    Osoba *o3 = new Student("Kuba", 2000, 3.89);
    Pracownik *p1 = new Kierownik("Adam", 1990, 4128.78, "Informatyk");
    cout << o1->wiek() << endl;
    cout << p1->wiek() << endl;
    cout<<o1;

    vector<Osoba>listaOsob;
    listaOsob.push_back(Osoba("ala",2000));
    listaOsob.push_back(Osoba("ola",1990));
    listaOsob.push_back(Osoba("ela",1994));
    listaOsob.push_back(Osoba("mela",1980));
    listaOsob.push_back(Osoba("ela",2005));
    for(int i=0;i<listaOsob.size();i++)
    {
        cout<<listaOsob[i].toString()<<endl;
    }
    int najstarszyRok;
    int najmlodszyRok = listaOsob.begin()->getRokUrodzenia();
    string najmlodszeImie;
    string najstarszeImie;
    for (Osoba osoba: listaOsob) {
        int rok = osoba.getRokUrodzenia();
        if (rok > najstarszyRok) {
            najstarszyRok = rok;
            najstarszeImie = osoba.toString();
        }
        if (rok < najmlodszyRok) {
            najmlodszyRok = rok;
            najmlodszeImie = osoba.toString();
        }
    }
    cout << "Najstarsza osoba: " << najstarszeImie << endl;
    cout << "Najmlodsza osoba: " << najmlodszeImie << endl;
    return 0;
}

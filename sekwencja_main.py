class Sekwencja:
    slots = '__sekwencja', '__dlugosc'

    def __init__(self, sekwencja: str):
        self.__sekwencja = ''.join(x.upper() for x in sekwencja if x.isalpha())
        self.__dlugosc = len(self.__sekwencja)

    def __add__(self, other: 'Sekwencja'):
        return Sekwencja(self.__sekwencja + other.__sekwencja)

    def length(self):
        if self.__dlugosc != len(self.__sekwencja):
            self.__dlugosc = len(self.__sekwencja)

        return self.__dlugosc

    def reverse(self):
        return self.__sekwencja[::-1]

    def __str__(self):
        return "Sekwencja: {}\nDlugosc: {}".format(self.__sekwencja, self.__dlugosc)

    def __getitem__(self, klucz: int):
        if klucz < 0 or klucz >= self.__dlugosc:
            raise IndexError("Niepoprawny przedzial! Sprobuj <0, {}>".format(self.__dlugosc))

        return self.__sekwencja[klucz]

    def __contains__(self, element: str):
        return element in self.__sekwencja

    def __eq__(self, other: 'Sekwencja'):
        return self.__dlugosc == other.__dlugosc and self.__sekwencja == other.__sekwencja


class NazwanaSekwencja(Sekwencja):
    slots = '__name'

    def __init__(self, sekwencja: str, name: str):
        Sekwencja.__init__(self, sekwencja)

        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

    def __str__(self):
        return "[Name: {}]\n{}".format(self.name, Sekwencja.__str__(self))

def main():
    # Podpunkt A
    L = []
    for i in range(5):
        nazwa = chr(ord('a') + i)

        print("Podaj lancuch sekwencji dla {}:".format(nazwa))
        lancuch = input()

        L.append(NazwanaSekwencja(lancuch, nazwa))
        # print(L[i])

    # Podpunkt B
    for element in L:
        if element.length() == 5:
            print(element)

    # Podpunkt C
    try:
        a = int(input("Podaj indeks pierwszej sekwencji: "))
        b = int(input("Podaj indeks drugiej sekwencji: "))
    except ValueError:
        print("Indeks musi byc liczba calkowita!")
        return

    if a < 0 or a >= 5 or b < 0 or b >= 5:
        print("Niepoprawny przedzial! Musi byc <0, 5]")
        return

    c = L[a] + L[b]
    print(c.reverse())

    # Podpunkt D
    for i in range(4):
        if L[i] == L[4]:
            print("Jest rowna ostatniej {}".format(L[i]))

    # Podpunkt E
    for element in L:
        first_letter = L[0][0]

        if first_letter in element:
            print("Element {} zawiera w sobie pierwszy znak z sekwencji o indeksie 0!".format(element.name))

    # Podpunkt J
    for element in L:
        element.name = element.name.upper()

    # Podpunkt K
    try:
        del L[0].__name

        print("Udało się usunąć '__name'")

    except Exception:
        print("Nie udało się usunąć '__name'")


if __name__ == '__main__':
    main()
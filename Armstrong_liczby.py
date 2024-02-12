# Liczby Armstronga to N-cyfrowa liczba naturalna która jest sumą swoich cyfr
# podniesionych do potęgi N. Na przykład: 153 = 13+53+33.
# Proszę napisać program znajdujący jak najwięcej takich liczb.

zakres_liczb = int(input("Podaj liczbę,dla której będzie wykorzystany program: "))

for i in range(10, zakres_liczb):
    dlugosc = len(str(i))
    potega = int(dlugosc)
    suma_cyfr = 0
    liczba = i

    # wyodrębniam cyfrę
    while liczba > 0:
        # dzielę przez 10 i obliczam resztę z dzielnia, by uzyskać ostatnią cyfrę liczby
        cyfra = liczba % 10
        # podnoszę do potęgi, a następnie dodaję do sumy
        suma_cyfr += pow(cyfra, potega)
        liczba //= 10

    # jeśli warunek zostanie spełniony == liczbą Armstronga
    if i == suma_cyfr:
        # Program wypisze liczbę
        print(i)
# Na zakończenie komunikat
input("Aby zakończyć program naciśnij Enter")

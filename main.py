import numpy
import pandas as pd
import math
import matplotlib
import matplotlib.pyplot as plt


dane = pd.read_csv("data.csv", header=None)
liczba_gatunkow = 3
liczba_rekordow = len(dane)


def zliczanie(lista):
    pom = [0, 0, 0]
    for i in range(len(lista)):
        pom[lista[i]] += 1
    return pom


def udzial_procentowy(lista):
    for i in range(liczba_gatunkow):
        print(round(lista[i] / liczba_rekordow * 100, 1), "%")


def maksimum(lista):
    wartosc = lista[0]
    for i in range(len(lista)):
        if lista[i] > wartosc:
            wartosc = lista[i]
    return round(wartosc, 2)


def minimum(lista):
    wartosc = lista[0]
    for i in range(len(lista)):
        if lista[i] < wartosc:
            wartosc = lista[i]
    return round(wartosc, 2)


def srednia(lista):
    suma = 0
    for wiersz in lista:
        suma += wiersz
    srednia = suma / len(lista)
    srednia = round(srednia, 2)
    return srednia


def mediana(lista):
    if type(lista) == pd.Series:
        lista = lista.tolist()
    lista.sort()
    if len(lista) % 2 == 0:
        med = (lista[int(len(lista) / 2)] + lista[int(len(lista) / 2) - 1]) / 2
    else:
        med = lista[int(len(lista) / 2)]
    return round(med)


def kwartyl(lista, nr_kwartylu):
    if type(lista) == pd.Series:
        lista = lista.tolist()
    lista.sort()
    kwartyl = lista[int(nr_kwartylu / 4 * len(lista))]
    # print(int(nr_kwartylu/4*len(lista))+1)
    return round(kwartyl, 2)


def odchylenie_standardowe(lista):
    if type(lista) == pd.Series:
        lista = lista.tolist()
    avg = srednia(lista)
    pom = 0
    for i in range(len(lista)):
        pom += (lista[i] - avg) ** 2
    pom /= len(lista)
    pom = math.sqrt(pom)
    return round(pom, 2)


tablica = []
for i in range(5):
    tablica.append(dane[i])
print(tablica)
for i in range(4):
    print(i)
    print("max", maksimum(tablica[i]), "\tmin", minimum(tablica[i]))
    print("avg", srednia(tablica[i]), "\tmed", mediana(tablica[i]))
    print("kw1", kwartyl(tablica[i], 1), "\tkw3", kwartyl(tablica[i], 3))
    print("oSt", odchylenie_standardowe(tablica[i]))
    plt.hist(tablica[i], bins=8)
    plt.show()
    plt.boxplot(tablica[i], positions=[1, 4])
    plt.show()
gatunki = zliczanie(tablica[4])
print(gatunki)
udzial_procentowy(gatunki)

# kwartyl1(tablica[0])
# print(max(dane[i]), "\t", min(dane[i]), "\t", )
# print("\n")
# print(dane)

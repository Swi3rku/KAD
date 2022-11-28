import pandas as pd
import math
import matplotlib.pyplot as plt


dane = pd.read_csv("data.csv", header=None)
liczba_gatunkow = 3
liczba_rekordow = len(dane)
setosa = dane.loc[dane.iloc[:, 4] == 0]
versicolor = dane.loc[dane.iloc[:, 4] == 1]
virginica = dane.loc[dane.iloc[:, 4] == 2]


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
    return round(med, 2)


def kwartyl(lista, nr_kwartylu):
    if type(lista) == pd.Series:
        lista = lista.tolist()
    lista.sort()
    kwartyl = lista[int(nr_kwartylu / 4 * len(lista))]
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

plt.figure(figsize=(5,4),dpi=300)
plt.scatter(dane[0],dane[1],s=80)
plt.xticks(ticks=[4,5,6,7,8])
plt.savefig("probny",dpi=300)
plt.show()
plt.figure(figsize=(5,4),dpi=300)
plt.scatter(dane[0],dane[2],s=80)
plt.xticks(ticks=[4,5,6,7,8])
plt.show()
plt.figure(figsize=(5,4),dpi=300)
plt.scatter(dane[0],dane[3],s=80)
plt.xticks(ticks=[4,5,6,7,8])
plt.show()



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




zDlugoscDzialkiK = [4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0]
zSzerokoscDzialkiK = [2.0,2.2,2.4,2.6,2.8,3.0,3.2,3.4,3.6,3.8,4.0]
zDlugoscPlatka = [1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0]
zSzerokoscPlatka = [0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2]
zakres = [zDlugoscDzialkiK,zSzerokoscDzialkiK,zDlugoscPlatka,zSzerokoscPlatka]
title = ['Długość działki kielicha','Szerokość działki kielicha','Długość płatka','Szerokość płatka']
podpisXb=['setosa','versicolor','virginica']
podpisXh=['Długość (cm)', 'Szerokość (cm)','Długość (cm)', 'Szerokość (cm)']
podpisYh='Liczebność'
plikName = ["DlugoscDzialkiK.jpg","SzerokoscDzialkiK.jpg","DlugoscPlatka.jpg","SzerokoscPlatka.jpg"]
plikboxName =["DlugoscDzialkiGat.jpg","SzerokoscDzialkiGat.jpg","DlugoscPlatkaGat.jpg","SzerokoscPlatkaGat.jpg"]
for i in range(4):
    plt.figure(figsize=(5,4),dpi=300)
    plt.title(title[i])
    plt.xlabel(podpisXh[i])
    plt.ylabel(podpisYh)
    plt.xticks(zakres[i])
    plt.hist(dane[i],bins=zakres[i],edgecolor="black")
    plt.savefig(plikName[i],dpi=300)
    plt.figure(figsize=(5,4),dpi=300)
    plt.boxplot([setosa[i], versicolor[i], virginica[i]], labels=podpisXb)
    plt.savefig(plikboxName[i],dpi=300)
    plt.figure(figsize=(5,4),dpi=300)
    plt.xlabel(podpisXh[i])
    plt.ylabel(podpisYh)
    plt.xticks(zakres[i])
    plt.title(title[i])
    plt.hist(setosa[i],bins=zakres[i],alpha=0.3,edgecolor="magenta",label="Setosa")
    plt.hist(versicolor[i], bins=zakres[i], alpha=0.3, edgecolor="darkred", label="Versicolor")
    plt.hist(virginica[i], bins=zakres[i], alpha=0.3, edgecolor="darkgreen", label="Virginica")
    plt.legend()
    plt.savefig("Combined"+plikName[i],dpi=300)

gatunki = zliczanie(dane[4])
print("Liczność gatunków")
print(gatunki)
udzial_procentowy(gatunki)
for i in range(4):
   print(title[i])
   print("Maksimum", maksimum(dane[i]), "\tMinimum", minimum(dane[i]))
   print("średnia", srednia(dane[i]), "\tmediana", mediana(dane[i]))
   print("Q1", kwartyl(dane[i], 1), "\t\t\tQ2", kwartyl(dane[i], 3))
   print("odch. stand. ", odchylenie_standardowe(dane[i]))

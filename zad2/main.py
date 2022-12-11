import pandas as pd
import math
import matplotlib.pyplot as plt


dane = pd.read_csv("data.csv", header=None)
liczba_gatunkow = 3
liczba_rekordow = len(dane)
setosa = dane.loc[dane.iloc[:, 4] == 0]
versicolor = dane.loc[dane.iloc[:, 4] == 1]
virginica = dane.loc[dane.iloc[:, 4] == 2]

def srednia(lista):
    suma = 0
    for wiersz in lista:
        suma += wiersz
    srednia = suma / len(lista)
    return srednia

def odchylenie_standardowe(lista):
    if type(lista) == pd.Series:
        lista = lista.tolist()
    avg = srednia(lista)
    pom = 0
    for i in range(len(lista)):
        pom += (lista[i] - avg) ** 2
    pom /= len(lista)
    pom = math.sqrt(pom)
    return pom

def suma(lista):
    suma=0
    for x in range(len(lista)):
        suma+=lista[x]
    return suma

def sumaKwadratow(lista):
    suma=0;
    for x in range(len(lista)):
        suma+=lista[x]**2
    return suma

def wspolczynnikKorelacjiLiniowejPearsona(listaX, listaY):
    odchylenieX = odchylenie_standardowe(listaX)
    odchylenieY = odchylenie_standardowe(listaY)
    sredniaX = srednia(listaX)
    sredniaY = srednia(listaY)
    kowariancja=0
    for i in range(len(listaX)):
        kowariancja+=(listaX[i] * listaY[i])
    kowariancja/=len(listaX)
    kowariancja-=(sredniaX*sredniaY)
    wsp=kowariancja/(odchylenieX*odchylenieY)
    return wsp

def wspolczynnik_A_RownaniaRegresjiLiniowej(listaX,listaY):
    sumaX=suma(listaX)
    kwadratSumyX = sumaX**2
    sumaY=suma(listaY)
    sumaKwadratowX = sumaKwadratow(listaX)
    sumaIloczynu = 0
    for x in range(len(listaX)):
        sumaIloczynu+=listaX[x]*listaY[x]
    a = ((len(listaX)*(sumaIloczynu))-(sumaX*sumaY))/((len(listaX)*sumaKwadratowX)-kwadratSumyX)
    return a

def wspolczynnik_B_RownaniaRegresjiLiniowej(listaX,listaY):
    sumaX=suma(listaX)
    kwadratSumyX = sumaX**2
    sumaY=suma(listaY)
    sumaKwadratowX = sumaKwadratow(listaX)
    sumaIloczynu = 0
    for x in range(len(listaX)):
        sumaIloczynu+=listaX[x]*listaY[x]
    b = ((sumaY*sumaKwadratowX)-(sumaX*sumaIloczynu))/((len(listaX)*sumaKwadratowX)-kwadratSumyX)
    return b

podpis = ["Długość działki kielicha (cm)","Szerokość działki kielicha (cm)", "Długość płatka (cm)","Szerokość płatka (cm)"]
#for i in range(4):
#    plt.figure(figsize=(5,4),dpi=300)
#    #plt.title(title[i])
#    plt.scatter(dane[0],dane[1],s=80)

#Atrybuty (kolumny):
#0. długość działki kielicha (ang. sepal length) [cm]
#1. szerokość działki kielicha (ang. sepal width) [cm]
#2. długość płatka (ang. petal length) [cm]
#3. szerokość płatka (ang. petal width) [cm]
#4. gatunek (ang. species):
#   0 - setosa
#   1 - versicolor
#   2 - virginica
# wykresy z x na Długość działki kielicha
plt.figure(figsize=(5,4),dpi=300)
plt.scatter(dane[0],dane[1],s=80)
plt.xticks(ticks=[4,5,6,7,8])
plt.xlabel(podpis[0]);
plt.ylabel(podpis[1])
plt.show()
plt.figure(figsize=(5,4),dpi=300)
plt.scatter(dane[0],dane[2],s=80)
plt.xticks(ticks=[4,5,6,7,8])
plt.xlabel(podpis[0]);
plt.ylabel(podpis[2])
plt.show()
plt.figure(figsize=(5,4),dpi=300)
plt.scatter(dane[0],dane[3],s=80)
plt.xticks(ticks=[4,5,6,7,8])
plt.xlabel(podpis[0]);
plt.ylabel(podpis[3])
plt.show()
#wykresy z x na Szerokość działki kielicha
plt.figure(figsize=(5,4),dpi=300)
plt.scatter(dane[1],dane[2],s=80)
plt.xticks(ticks=[4,5,6,7,8])
plt.xlabel(podpis[1]);
plt.ylabel(podpis[2])
plt.show()
plt.figure(figsize=(5,4),dpi=300)
plt.scatter(dane[1],dane[3],s=80)
plt.xticks(ticks=[4,5,6,7,8])
plt.xlabel(podpis[1]);
plt.ylabel(podpis[3])
plt.show()
#wykres z x na Długość płatka (cm)
plt.figure(figsize=(5,4),dpi=300)
plt.scatter(dane[2],dane[3],s=80)
plt.xticks(ticks=[4,5,6,7,8])
plt.xlabel(podpis[2]);
plt.ylabel(podpis[3])
plt.show()

for i in range(5):
    for j in range(i+1,4):
        print(i,j)
        print(wspolczynnikKorelacjiLiniowejPearsona(dane[i],dane[j]))
        print(wspolczynnik_A_RownaniaRegresjiLiniowej(dane[i],dane[j]))
        print(wspolczynnik_B_RownaniaRegresjiLiniowej(dane[i],dane[j]))


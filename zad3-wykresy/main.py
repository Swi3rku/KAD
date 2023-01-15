import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np


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
    suma=0
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


labels = ["DDK_SDK","DDK_DP","DDK_SP","SDK_DP","SDK_SP","DP_SP"]
x = [np.linspace(4,8,5), np.linspace(2,4.5,6), np.linspace(1,7,7)]
pom=0
probne = [[1,2,3,4,5,6,7],[32,51,13,12,32,4,43],[32,21,31,33,13,16,9],[3,4,2,5,6,7,9]]
for i in range(5):
    for j in range(i+1,4):
        pom+=1

plt.figure(figsize=(5,4),dpi=300)
#grupa + kolor
plt.scatter(probne[0],probne[1],s=80, color='red',label="grupa 1")
#poprostu tworzymy kolejne wykresy i dajemy dla nich kolor, 
#można potem ewentualnie dodać legende, wtedy dajemy label="nazwa"
plt.scatter(probne[2],probne[3],s=80, color='green',label="grupa 2")
#znacznik pozycji 'średniej' grupy
plt.scatter([2],[3],s=80, color='green',marker='d',label="grupa 2")
#i tak generujemy
plt.legend()
#plt.scatter(dane[i],dane[j],s=80)
#plt.scatter(dane[i],dane[j],s=80)
#plt.xlabel(podpis[i])
#plt.ylabel(podpis[j])
#plt.savefig(labels[pom])
plt.show()



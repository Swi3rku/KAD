import pandas as pd
import math
import random
import numpy as np
from matplotlib import pyplot as plt

liczba_klastrow = 3
dane = pd.read_csv("data_test.csv", header=None)

    # centroidy = []
    # klastry = []
    # for i in range(liczba_klastrow):
    #     klastry.append([])

def odleglosc(pkt1, pkt2):
    return math.sqrt((pkt2[0]-pkt1[0])**2+(pkt2[1]-pkt1[1])**2)

def losoweCentroidy(lista, centroidy):
    for i in range(liczba_klastrow):
        centroidy.append(random.choice(lista))
    print("centroidy",centroidy)



def k_srednich(lista1, lista2):
    # lista = list(zip(lista1, lista2))

    centroidy = []
    klastry = []
    for i in range(liczba_klastrow):
        klastry.append([])

    lista = []
    for i in range(len(dane[0])):
        pom=[]
        pom.append(lista1[i])
        pom.append(lista2[i])
        lista.append(pom)


    #1. początkowe położenia centroidów
    losoweCentroidy(lista, centroidy)

    #2. przypisanie punktowi najbliższego centroida
    for i in range(len(lista)):
        odleglosci_od_centroidow = []
        for j in range(liczba_klastrow):
            # print(odleglosc(lista[i],centroidy[j]))
            odleglosci_od_centroidow.append(odleglosc(lista[i],centroidy[j]))
        # print("min",min(odleglosci_od_centroidow))
        # print("index", odleglosci_od_centroidow.index(min(odleglosci_od_centroidow)))
        klastry[odleglosci_od_centroidow.index(min(odleglosci_od_centroidow))].append(lista[i])
    print("klastry1", klastry[0])
    print("klastry2", klastry[1])
    print("klastry3", klastry[2])
    print("centroidy", centroidy)

    #3. aktualizacja położenia centroidów
    # for k in range(liczba_klastrow):
    noweCentroidy = []
    pierwszeWejscie=True
    while(centroidy!=noweCentroidy):
        if(pierwszeWejscie==False):
            for k in range(len(centroidy)):
                centroidy[k]=noweCentroidy[k]
            noweCentroidy=[]
        for i in range(liczba_klastrow):
            avgX = 0
            avgY = 0
            for j in range(len(klastry[i])):
                avgX+=klastry[i][j][0]
                avgY+=klastry[i][j][1]
            avgX/=len(klastry[i])
            avgX=round(avgX,2)

            avgY/=len(klastry[i])
            avgY=round(avgY,2)
            noweCentroidy.append([avgX,avgY])
        pierwszeWejscie=False
    return centroidy, klastry

def doWykresu(lista):
    x=[]
    y=[]
    for i in lista:
        x.append(i[0])
        y.append(i[1])
    print("x", x)
    print("y", y)
    return x,y




for i in range(4):
    for j in range(i+1,4):
        centroidy, klastry = k_srednich(dane[i], dane[j])
        print("i",i," j",j)
        x,y = doWykresu(klastry[0])
        plt.figure(figsize=(5,4),dpi=300)
        #grupa + kolor
        plt.scatter(x,y,s=80, color='red',label="grupa 1")
        plt.scatter(centroidy[0][0],centroidy[0][1],s=80, color='red',label="grupa 1", marker="D", edgecolor="black")

        x,y = doWykresu(klastry[1])
        #grupa + kolor
        plt.scatter(x,y,s=80, color='green',label="grupa 2")
        plt.scatter(centroidy[1][0],centroidy[1][1],s=80, color='green',label="grupa 2", marker="D", edgecolor="black")
        x,y = doWykresu(klastry[2])
        #grupa + kolor
        plt.scatter(x,y,s=80, color='yellow',label="grupa 3")
        plt.scatter(centroidy[2][0],centroidy[2][1],s=80, color='yellow',label="grupa 3", marker="D", edgecolor="black")
        # plt.legend()
        plt.show()



#
# k_srednich(dane[2], dane[3])
# # print("i",i," j",j)
# x,y = doWykresu(klastry[0])
# plt.figure(figsize=(5,4),dpi=300)
# #grupa + kolor
# plt.scatter(x,y,s=80, color='red',label="grupa 1")
# plt.scatter(centroidy[0][0],centroidy[0][1],s=80, color='red',label="grupa 1", marker="D", edgecolor="black")
# x,y = doWykresu(klastry[1])
# #grupa + kolor
# plt.scatter(x,y,s=80, color='green',label="grupa 2")
# plt.scatter(centroidy[1][0],centroidy[1][1],s=80, color='green',label="grupa 2", marker="D", edgecolor="black")
# x,y = doWykresu(klastry[2])
# #grupa + kolor
# plt.scatter(x,y,s=80, color='yellow',label="grupa 3")
# plt.scatter(centroidy[2][0],centroidy[2][1],s=80, color='yellow',label="grupa 3", marker="D", edgecolor="black")
# # plt.legend()
# plt.show()
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
    return math.sqrt((pkt2[0]-pkt1[0])**2+(pkt2[1]-pkt1[1])**2+(pkt2[2]-pkt1[2])**2+(pkt2[3]-pkt1[3])**2)

def losoweCentroidy(lista, centroidy):
    for i in range(liczba_klastrow):
        centroidy.append(random.choice(lista))
    print("centroidy",centroidy)

def przypisanieDoKlastrow(klastry, lista, centroidy):
    klastry=zerowanieKlastrow(klastry)
    for i in range(len(lista)):
        odleglosci_od_centroidow = []
        for j in range(liczba_klastrow):
            # print(odleglosc(lista[i],centroidy[j]))
            odleglosci_od_centroidow.append(odleglosc(lista[i],centroidy[j]))
        # print("min",min(odleglosci_od_centroidow))
        # print("index", odleglosci_od_centroidow.index(min(odleglosci_od_centroidow)))
        klastry[odleglosci_od_centroidow.index(min(odleglosci_od_centroidow))].append(lista[i])
    return klastry

def zerowanieKlastrow(klastry):
    klastry = []
    for i in range(liczba_klastrow):
        klastry.append([])
    return klastry

def k_srednich(lista1, lista2, lista3, lista4):
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
        pom.append(lista3[i])
        pom.append(lista4[i])
        lista.append(pom)


    #1. początkowe położenia centroidów
    losoweCentroidy(lista, centroidy)

    #2. przypisanie punktowi najbliższego centroida
    klastry=przypisanieDoKlastrow(klastry, lista, centroidy)
    print("klastry1",klastry[0],'\n')
    print("klastry2",klastry[1],'\n')
    print("klastry3",klastry[2],'\n')

    #3. aktualizacja położenia centroidów
    # for k in range(liczba_klastrow):
    noweCentroidy = []
    pierwszeWejscie=True
    while(centroidy!=noweCentroidy):
        if(pierwszeWejscie==False):
            for k in range(len(centroidy)):
                centroidy[k]=noweCentroidy[k]
            klastry=przypisanieDoKlastrow(klastry, lista, centroidy)
            noweCentroidy=[]
        for i in range(liczba_klastrow):
            avgX = 0
            avgY = 0
            avgZ = 0
            avgW = 0
            for j in range(len(klastry[i])):
                avgX+=klastry[i][j][0]
                avgY+=klastry[i][j][1]
                avgZ+=klastry[i][j][2]
                avgW+=klastry[i][j][3]
            # if not klastry[i]:
            #     pom1=-1
            #     pom2=-1
            #     pom3=-1
            #     pom4=-1
            #     return pom1,pom2,pom3,pom4
            # print("klastry[i]",klastry[i])
            # print(len(klastry[i]))
            avgX/=len(klastry[i])
            avgX=round(avgX,2)

            avgY/=len(klastry[i])
            avgY=round(avgY,2)

            avgZ/=len(klastry[i])
            avgZ=round(avgZ,2)

            avgW/=len(klastry[i])
            avgW=round(avgW,2)
            noweCentroidy.append([avgX,avgY,avgZ,avgW])
        pierwszeWejscie=False
    return centroidy, klastry

def doWykresu(lista):
    x=[]
    y=[]
    z=[]
    w=[]
    for i in lista:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
        w.append(i[3])
    # print("x", x)
    # print("y", y)
    return x,y,z,w

# def test(lista1, lista2, lista3, lista4):
#     pom1 = -1
#     pom2 = -1
#     while(pom1==-1 or pom2==-1):
#         pom1, pom2 = k_srednich(lista1, lista2, lista3, lista4)
#     return pom1,pom2

centroidy, klastry = k_srednich(dane[0], dane[1], dane[2],dane[3])
print("centr", centroidy)
tmp = []
for i in range(3):
    pom=[]
    x,y,z,w = doWykresu(klastry[i])
    pom.append(x)
    pom.append(y)
    pom.append(z)
    pom.append(w)
    tmp.append(pom)
print("tmp",tmp)
for i in range(4):
    for j in range(i+1,4):

        # centroidy, klastry = test(dane[i], dane[j])
        print("i",i," j",j)

        plt.figure(figsize=(5,4),dpi=300)
        # #grupa + kolor
        plt.scatter(tmp[0][i],tmp[0][j],s=80, color='red',label="grupa 1")
        plt.scatter(centroidy[0][i],centroidy[0][j],s=80, color='red',label="grupa 1", marker="D", edgecolor="black")
        #
        #
        # #grupa + kolor
        plt.scatter(tmp[1][i],tmp[1][j],s=80, color='green',label="grupa 2")
        plt.scatter(centroidy[1][i],centroidy[1][j],s=80, color='green',label="grupa 2", marker="D", edgecolor="black")

        #grupa + kolor
        plt.scatter(tmp[2][i],tmp[2][j],s=80, color='yellow',label="grupa 3")
        plt.scatter(centroidy[2][i],centroidy[2][j],s=80, color='yellow',label="grupa 3", marker="D", edgecolor="black")
        plt.show()


# centroidy, klastry = k_srednich(dane[0], dane[1], dane[2],dane[3])
# print("cent",centroidy)
# # centroidy, klastry = test(dane[i], dane[j])
# # print("i",i," j",j)
# x,y = doWykresu(klastry[0])
# plt.figure(figsize=(5,4),dpi=300)
# #grupa 1
# plt.scatter(x,y,s=80, color='red',label="grupa 1")
# plt.scatter(centroidy[0][0],centroidy[0][1],s=80, color='red',label="grupa 1", marker="D", edgecolor="black")
# #grupa2
# x,y = doWykresu(klastry[1])
# plt.scatter(x,y,s=80, color='green',label="grupa 2")
# plt.scatter(centroidy[1][0],centroidy[1][1],s=80, color='green',label="grupa 2", marker="D", edgecolor="black")
# #grupa3
# x,y = doWykresu(klastry[2])
# plt.scatter(x,y,s=80, color='yellow',label="grupa 3")
# plt.scatter(centroidy[2][0],centroidy[2][1],s=80, color='yellow',label="grupa 3", marker="D", edgecolor="black")
# plt.show()

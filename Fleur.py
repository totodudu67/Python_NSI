# Créé par t.dupuy, le 16/05/2023 en Python 3.7
import pandas
import csv
import matplotlib.pyplot as plt
import math

iris = pandas.read_csv("iris.csv")
x = iris.loc[:,"longueur_petale"]
y = iris.loc[:,"largeur_petale"]
lab = iris.loc[:,"espece"]
liste = list(zip(x,y,lab))
echan = [float(input("x : ")), float(input("y")), str(input("espece"))]


##echan = [0, 0, None]
##liste = list(zip(x, y, lab))
##echan[0] = float(input("Entrez la valeur de la largeur du pétale : "))
##echan[1] = float(input("Entrez la valeur de la longueur du pétale : "))
##nouvel_echan = [echan[0], echan[1], None]

def dist_euclid(echan, liste):
    dist = []
    for i in range(len(liste)):
        distance = ((echan[0] - liste[i][0])**2 + (echan[1] - liste[i][1])**2)**0.5
        dist.append([distance, liste[i][2]])
        dist = sorted(dist)
    return dist

dist_triees = dist_euclid(echan, liste)

##dist_triees = sorted(distances)

def KNN(dist_triees, k):
    voisins = [[0, 0], [1, 0], [2, 0]]
    max = 0
    for i in range(k):
        if dist_triees[i][1] == 0:
            voisins[0][1] += 1
        elif dist_triees[i][1] == 1:
            voisins[1][1] += 1
        elif dist_triees[i][1] == 2:
            voisins[2][1] += 1
    for i in range(len(voisins)):
        if voisins[i][1] > max:
            max = voisins[i][1]
            echan = voisins[i][0]
    print(voisins)
    if echan == 0:
        esp = "setosa"
        couleur = 'g'
    elif echan == 1:
        esp = "virginica"
        couleur = 'r'
    elif echan == 2:
        esp = "versicolor"
        couleur = 'b'
    print("L'espèce est sûrement", esp)
    return couleur

couleur = KNN(dist_triees, 5)

##truc = KNN(dist_triees, k)
####k = int(input("Entrez la valeur de k : "))
##nouvel_echan = KNN(dist_triees, k)
##couleur = nouvel_echan[2]

plt.scatter(x[lab==0], y[lab==0], s=10, marker='^', color='g', label='setosa')
plt.scatter(x[lab==1], y[lab==1], s=10, marker='*', color='r', label='virginica')
plt.scatter(x[lab==2], y[lab==2], s=10, marker=',', color='b', label='versicolor')
plt.scatter(echan[0], echan[1], s=40, marker='x', color=couleur, label=echan[2])
plt.legend()
plt.show()

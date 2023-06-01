# Sudoku 4x4 - MP_Spé_NSI
# coding -*- utf-8 -*-
import random
from math import sqrt
# Création de la grille ________________________________________

S = [
    [1, 0, 3, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]



# La fonction ligne ____________________________________________
def ligne(S, i) :

    """ renvoie la liste des chiffres d'une ligne i de S
        param S(list) la grille de sudoku
        param i(int) une ligne de la grille
        return l(list) ensemble des chiffres présents sur la ligne i
        de la grille S
    """
    assert 0 <= i < len(S), "L'indice de ligne est invalide"
    l = []
    for j in range(len(S[i])):
        if S[i][j] != 0:
            l.append(S[i][j])
    return l

# ASSERTION sur i

# CODE de la fonction ligne
##    l = ...
##    for j in ... :
##        if S[i]...
##            l. ...
##    return l

# La fonction colonne ___________________________________________
def colonne(S, j) :

    """ renvoie la liste des chiffres d'une colonne j de S
        param S(list) la grille de sudoku
        param j(int) une colonne de la grille
        return l(list) ensemble des chiffres présents sur la colonne j
        de la grille S
    """
    assert 0 <= j < len(S[0]), "L'indice de colonne est invalide"
    l = []
    for i in range(len(S)):
        if S[i][j] != 0:
            l.append(S[i][j])
    return l

# ASSERTION sur j

# CODE de la fonction colonne


# La fonction bloc ______________________________________________
def bloc(S, i, j) :
    """ renvoie la liste des chiffres d'un bloc identifier par l'une
        de ses cases (i, j)
        param S(list) la grille de sudoku
        param i(int) une ligne de la grille
        param j(int) une colonne de la grille
        return l(list) ensemble des chiffres présent dans le bloc
    """
    l = []
    # calcul de h et g
    h = (i // int(sqrt(len(S)))) * int(sqrt(len(S)))
    g = (j // int(sqrt(len(S[0])))) * int(sqrt(len(S[0])))
    # taille du côté du bloc carré
    t = int(sqrt(len(S)))
##    for ligne in (...) :
##        for colonne ...
    for x in range(h, h + t):
        for y in range(g, g + t):
            if S[x][y] != 0:
                l.append(S[x][y])
    return l

# La fonction possibles ________________________________________________
def possibles (S, i, j) :
    """ Renvoie la liste des chiffres possibles pour une case donnée
    """
    assert 0 <= i < len(S) and 0 <= j < len(S[0]), "Les indices de ligne et de colonne sont invalides"
    chiffres_possibles = [1, 2, 3, 4]
    chiffres_presents = ligne(S, i) + colonne(S, j) + bloc(S, i, j)
    return [x for x in chiffres_possibles if x not in chiffres_presents]

# La fonction suivante __________________________________________________
def suivante (i, j) :
    """ calcule les coordonnées de la case suivante
        param i(int) la ligne de la case actuelle
        param j(int) la colonne de la case actuelle
        return k(int) ligne de la case suivante
        return l(int) colonne de la case suivante
    """
    if j < 3:
        k = i
        l = j + 1
    elif j == 3:
        k = i + 1
        l = 0
    return (k, l)


#La fonction résolution _____________________________________________
def resolution (S, i, j) :
##    affiche()
##    if i == ... :
##        return True
##    elif ... :
##        k, l = ...
##        return resolution(S, k, l)
##    elif ...
##        for x in ...:
##            S[i][j] = ...
##            k, l = ...
##            if resolution(S, k, l) == True :
##                return True
##    S[i][j] = 0
##    return False

    affiche()
    if i == 4:
        return True
    elif S[i][j] != 0:
        k, l = suivante(i, j)
        return resolution(S, k, l)
    else:
        for x in possibles(S, i, j):
            S[i][j] = x
            k, l = suivante(i, j)
            if resolution(S, k, l) == True:
                return True
    S[i][j] = 0
    return False

# Affichage console __________________________________________________
def affiche() :
    a='\n'
    for i in range (len(S[0])) :
        for j in range (len(S)) :
            a = a + str(S[i][j]) + "\t"
        a = a + "\n"
    print(a)

resolution (S,0,0)

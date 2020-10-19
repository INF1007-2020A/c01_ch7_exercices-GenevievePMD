#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi
from turtle import pendown, penup, setpos, back, forward, left, right, color
    # 3 premiers sont pour le tronc
    # back = prend curseur et fait trait par en arrière
    # forward = dessin vers l'avant
    # left : tounrer curseur vers la gauche avec angle spécifié
    # right : tourner curseur vers la droite avec angle spécifié
    # left/right ne dessine pas


from ch6 import histogram   # fonction qui retourne un dictionnaire

MAX_DEPTH = 4
BRANCH_LENGTH = 100
SHRINK_FACTOR = 0.8
TURN_ANGLE = 20 # degrees


# TODO: Définissez vos fonction ici
# Exercice 1 - Retourner la masse et le volume d'un ellisoide
def ellipsoide(a :float= 1, b :float= 1, c :float= 1, masse_volumique :float= 1) -> tuple: # Par défaut, les demi-axes et masse volumique ont des valeurs de 1
    volume = (4/3) * pi * a * b * c
    masse = volume * masse_volumique
    return masse, volume

# Exercice 2 - À Compléter - Avec import ch6
def sort(sequence : str) -> tuple:
    dict_sequence = {}

    # return sorted(histogram(sequence).items(), reverse = True, key = lambda x:x[1])[0]  # inversé l'ordre les éléments avec le reverse
    # prendre le premier élément d,une séquence inversée. revient à prendre le dernier élément d'une séquence normale.
    #équivalent
    return sorted(histogram(sequence).items(), key = lambda x:x[1])[-1] # histogram est un dictionnaire. pour ça que peut faire .items



# Exercice 3 - Dessiner un arbre en utilisant la récursivité

def draw_trunk() -> None:
    color('green')
    left(90)    # Arbre à 90 degrées, donc perpendiculaire au sol. "debout"
    penup()
    setpos(x = 0, y = -200)
    pendown()
    forward(BRANCH_LENGTH)

def draw_left(depth : int, distance : float) -> None:
    left(TURN_ANGLE)
    forward(distance + SHRINK_FACTOR)

    draw_tree(depth + 1)    # sortir de la fonction draw_tree

    back(distance + SHRINK_FACTOR)  # retourner en arrière de la distance, faire la partie droite
    right(TURN_ANGLE)


def draw_right(depth : int, distance : float) -> None:
    right(TURN_ANGLE)
    forward(distance + SHRINK_FACTOR)

    draw_tree(depth + 1)    # sortir de la fonction draw_tree

    back(distance + SHRINK_FACTOR)  # retourner en arrière de la distance, faire la partie gauche
    left(TURN_ANGLE)



def draw_tree(depth : int) -> None:
    distance = BRANCH_LENGTH * SHRINK_FACTOR ** depth   # Distance doit diminuée car dans l'arbre, les branches plus loins, niveau plus élevé, doivent être plus petites

    if depth <= MAX_DEPTH : # Critère d'arrêt. quand rendu au bout de l'arbre, retourne au début
        draw_left(depth, distance)  # portion de gauche de l'arbre
        draw_right(depth, distance)



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    # Appel de la fonction de l'exercice 1 - Masse et volume de l'ellipsoide
    masse,volume = ellipsoide(1,5,6,10)
    print(f'Un ellipsoide a une masse de {round(masse,3)} kg et un volume de {round(volume,3)} m^3.')

    # Exercice 2
    print(sort("nyaaaan Cat"))

    # Exercice 3
    ''' Dessiner le tronc, côté gauche. et ensuite faire le côté droit. Continuer, revenir, continuer, revenir'''
    draw_trunk()
    draw_tree(0)    # Fonction récursive





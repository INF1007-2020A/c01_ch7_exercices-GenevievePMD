#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi
import turtle
import ch6


# TODO: Définissez vos fonction ici
# Exercice 1 - Retourner la masse et le volume d'un ellisoide
def ellipsoide(a :float= 1, b :float= 1, c :float= 1, masse_volumique :float= 1) -> tuple: # Par défaut, les demi-axes et masse volumique ont des valeurs de 1
    volume = (4/3) * pi * a * b * c
    masse = volume * masse_volumique
    return masse, volume

# Exercice 2 - À Compléter
# Avec import ch6


# Exercice 3 - Dessiner un arbre en utilisant la récursivité




if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    # Appel de la fonction de l'exercice 1 - Masse et volume de l'ellipsoide
    masse,volume = ellipsoide(1,5,6,10)
    print(f'Un ellipsoide a une masse de {round(masse,3)} kg et un volume de {round(volume,3)} m^3.')


    pass

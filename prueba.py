#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ejample.py
#
#  Copyright 2016 Braian Hernán Vicente <braianvicente@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

def main():
    print "holamundopython"
    for numero in range(10000) :
        if esNumeroPrimo(numero) :
            print numero, "Es Primo",'\a'
    print succesionFubinachiIterativa(5)

    return 0

def esNumeroPrimo(numeroPrimo) :
    """
    Funcion que determina si un numero es primo o no, esta optimizado
    para realizar una busqueda menor.
    """
    inicio = (numeroPrimo ** 0.5 )
#   numeroPrimo ** 0.5 es raiz cuadrada de numeroPrimo     

    inicio = int(inicio)
    while (inicio > 1) :
        if ( ( numeroPrimo % inicio ) == 0) :
            return False
        inicio = inicio - 1
    return True

def succesionFubinachiIterativa(numeroOrden):
    """
    Funcion que determina el numero n, de la orden de Fibbonachi de
    manera iterativa.
    """
    if (numeroOrden <= 3 ) :
        return numeroOrden
    fib_0 = 0
    fib_1 = 1
    aux = 0
    while (numeroOrden > 0 ) :
        aux = fib_0 + fib_1
        fib_0 = fib_1
        fib_1 = aux
        numeroOrden = numeroOrden - 1
    return aux

def succesionFubinachiRecursiva(numeroOrden):
    if (numeroOrden <= 3 ) :
        return numeroOrden
    fib_0 = 0
    fib_1 = 1
    aux = 0
    return succesionFubinachiRecursiva(numeroOrden - 1) + succesionFubinachiRecursiva(numeroOrden - 2)

if __name__ == '__main__':
    main()

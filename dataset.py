#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dataset.py
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
# Creates a simple random forest benchmark

import sys
LECTURA = 'r'
TEST = "test.csv"
TRAIN = "train.csv"

def cargarArchivo(entrada) :
    try:
        archivo = open(entrada,LECTURA)
        return archivo
    except:
        print "ERROR DE ARCHIVO."
        return False

def conocerCantidadSetDeDatos(entrada):
    indice = 0
    archivo = cargarArchivo(entrada)
    while archivo.readline() :
        indice = indice + 1
    print indice - 1
    return 0

def conocerCantidadSetDeDatosTest():
    return conocerCantidadSetDeDatos(TEST)

def conocerCantidadSetDeDatosTrain():
    return conocerCantidadSetDeDatos(TRAIN)

def main():
    conocerCantidadSetDeDatosTest()
    conocerCantidadSetDeDatosTrain()
    print "prueba sin password"


if __name__ == '__main__':
    main()


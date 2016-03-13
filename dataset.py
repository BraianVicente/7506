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
    archivo.close()
    return 0

def contarYMostrarClases(entrada):
    
    conjunto = set()
    archivo = cargarArchivo(entrada)
    linea = archivo.readline()
    for linea in archivo:
        conjunto.add(linea[0])
        
        
    conjunto = sorted(conjunto)
    print len(conjunto)
    print conjunto
    archivo.close()
    
def contarImagenesPorClase(entrada):
    cantidadImagenes = [0,0,0,0,0,0,0,0,0,0]
    archivo = cargarArchivo(entrada)
    linea = archivo.readline()
    for linea in archivo:
        cantidadImagenes[int(linea[0])] = cantidadImagenes[int(linea[0])] + 1
        
    print cantidadImagenes
    archivo.close()
    return cantidadImagenes

def contarCantidadPixel(entrada,cantidad) :
    cantidadZeros = [0,0,0,0,0,0,0,0,0,0]
    mayorCantidadZeros = [0,0,0,0,0,0,0,0,0,0]
    menorCantidadZeros = [255,255,255,255,255,255,255,255,255,255]
    archivo = cargarArchivo(entrada)
    archivo.readline()
    
    for linea in archivo :
        cadena = ""
        cantidadActualCero = 0
        for caracter in linea :
            if caracter != '\0' :
            
                if caracter != ',':
                    cadena = cadena + caracter
                else :
                    if 0 == int(cadena) :
                        cantidadZeros[int(linea[0])] = cantidadZeros[int(linea[0])] + 1
                        cantidadActualCero = cantidadActualCero + 1 
                                                
                    cadena = ""
                    cantidadActualCero = 0
        if mayorCantidadZeros[int(linea[0])] < cantidadActualCero :
            mayorCantidadZeros[int(linea[0])] = cantidadActualCero
        if menorCantidadZeros[int(linea[0])] > cantidadActualCero :
            menorCantidadZeros[int(linea[0])] = cantidadActualCero

       
    print cantidadZeros
    print mayorCantidadZeros
    print menorCantidadZeros
    
         
        
def main():
#    conocerCantidadSetDeDatos(TEST)
#    conocerCantidadSetDeDatos(TRAIN)
#    contarYMostrarClases(TRAIN)
    cantidad = contarImagenesPorClase(TRAIN)
    contarCantidadPixel(TRAIN,cantidad)
main()


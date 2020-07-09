# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
#Que determine si el estudiante esta aprobado o no

def determinaraprobado(promedio):
    if promedio>11:
        resultado="Aprobado"
    else:
        resultado="Desaprobado"
    return resultado

promedio = int(input("Promedio"))
print(determinaraprobado(5))
    
    

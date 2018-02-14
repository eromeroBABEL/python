#-*- coding: utf-8 -*-
"""
Listas y Tuplas
TUPLA: ('ejemplo1',34,'Eduardo',true). Menos recursos en memoria. Inmutable
LISTA: ['Eduardo',32,'Garrido']
"""

print "TUPLAS"
tupla=('uno',44,"prueba","final")
print tupla[1]
for x in tupla:
	print x

print "Porciones: ",tupla[1:3]
print "----------------------------------------------------------"

print "LISTAS"

lista=['prueba','Eduardo',343,'yuhuuu']

lista[3]="Me voy a enganchar" # Esto no podría hacerlo con una tupla

print lista
print "Longitud ";len(lista)

lista.append('added')
print lista
print "Longitud ",len(lista)

lista2=['hola', 99, 'adios']

lista.append(lista2)
print lista
print lista[5][2]

lista.pop()

print lista

print lista.index('Eduardo')

lista.reverse()

print lista

lista.sort()

print lista
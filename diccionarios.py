#-*- coding: utf-8 -*-
"""
DICCIONARIOS: Formado por clave:valor y va entre corchetes.

Ejemplo {'clave1':valor1, 'clave2':valor2}
del(mi_diccionario['clave1'] -> borra ese campo del diccionario

"""
diccionario={'clave1':'valor1', 'clave2':'valor2'}
import os # librería para trabajar con sistema operativo

lista=os.listdir('C:\Windows\System32')

for x in lista:
	if x[-3:]=="exe" or x[-3:]=="cmd" :
		print x


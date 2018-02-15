#-*- coding: utf-8 -*-

"""
FUNCIONES:
---------------------------------
def funcion1():
	comando1
	comando2
	[return valor] #Solo para funciones que devuelven un valor

	
"""

def imprimir(): #Procedimiento
	print "hola"
	
def funcion_holamundo(): #Funcion
	return "Hola Mundo"

def nombre(nombre,apellido):
	print nombre+" "+apellido

def parimpar(z1):
	"""
	if n1%2==0:
		return "par"
	else:
		return "impar"
	"""
	return "par" if(z1%2==0) else "impar"
	
	
def datos(dni,nombre,*apellidos):
	print "DNI: "+dni
	print "Nombre: "+nombre
	contador=1
	for a in apellidos:
		print "Apellido "+str(contador)+": "+a
		contador+=1
		
def iniciales(nombre,*apellidos):
	iniciales_lista=[]
	iniciales_lista.append(nombre[0])
	for x in apellidos:
		iniciales_lista.append(x[0])
		
	return iniciales_lista
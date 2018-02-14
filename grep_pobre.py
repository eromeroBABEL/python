#-*- coding: utf-8 -*-

"""
Programa: pedimos una letra por teclado y listamos los ficheros que tienen esa letra en el nombre
"""
import os
letra=raw_input("Que patron? ")

ficheros=os.listdir('C:\Windows\System32')
cuantos=0
for x in ficheros:
	if x.count(letra)>0:
		print x
		cuantos+=1
		
print " "
print "------------------------------------------------"
print "Hay "+str(cuantos)+" ficheros con '"+str(letra)+"'"
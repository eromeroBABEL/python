#Dos variables y pintar los numeros que hay entre ellas
#-*- coding: utf-8 -*-
n1=input("Numero uno? ")
n2=input("Numero dos? ")

for x in range(int(n1)+1,int(n2)):
	if int(x)%2==0:
		print x
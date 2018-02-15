import os,sys

def ver_version():
	return sys.version

"""
FICHEROS




"""

def crearDirectorio(path_file):
	if (os.access(path_file,1) == False):
		os.mkdir(path_file)
	else:
		print "Ya existe el directorio"
		

def VerVariablesEntorno():
#Funcion que devuevla el usuario, la shell y el path con el que estamos trabajando	
	for x,y in os.environ.iteritems():
		if x=="USER" or x=="PATH" or x=="SHELL":
			print x+"-->"+y
	print os.environ.get('USER')
	print os.environ.get('PATH')
	print os.environ.get('SHELL')
	

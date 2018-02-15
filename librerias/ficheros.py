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
		
	

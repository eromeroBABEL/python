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
	


def gordos(path_dir,size):
#Funcion que devuelva los ficheros que ocupan mas de un tamanio indicado
	if str(size).count("M"):
		size_final=int(str(size)[:-1])*1024*1024
	elif str(size).count("G"):
		size_final=int(str(size)[:-1])*1024*1024*1024
	else:
		size_final=size
	for x in os.listdir(path_dir):
		path_completo=path_dir+"/"+str(x)
		size_file=os.path.getsize(path_completo)
		if os.path.isfile(path_completo) and size_file>size_final:
			print x+" --> "+str(size_file)+" Bytes"


"""
LEER y ESCRIBIR en ficheros.
Objeto File : No es una libreria (No es necesario import)
f=open('f1.txt',w)
f.read([bytes])
f.readline([bytes]). Si no ponemos argumento lee una linea.
f.write("cadena")
f.writelines("secuencia")
f.close()
"""

def CatNombreFichero(path_fichero):
#Programa que acepte un nombre de fichero y lo lea
	if os.path.exists(path_fichero):
		f=open(path_fichero,'r')
		for x in f.readlines():
			print x[0:-1]
		f.close()

def cp(fichero1,fichero2):
	if os.access(fichero1,0):
		if os.path.isfile(fichero1)
			fich=open(fichero1,"r")
			fich2=open(fichero2,"w")
			while True:
		       		linea=fich.readline()
		       		if not linea: break;
		       		fich2.write(linea)
				fich2.close()
			fich.close()
		else:
			print("No es un fichero")
	else:
		print("Path no existe.")

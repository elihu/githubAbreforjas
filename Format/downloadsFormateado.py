#Cojo los datos de downloads de cada proyecto
import github
import sys
import codecs

def count(param):
   	acum = 0
	for a in param:
		acum = acum + 1
	return acum

if len(sys.argv) == 3: #Para poner un rango de usuarios que queremos ver
	i = int(sys.argv[1])
	j = int(sys.argv[2])
	
	datos = github.Github("usuario", "contraseña")
	repositorios = datos.get_repos()
	ficheroDownloads = codecs.open("downloads.csv", "w", "utf-8") #Abrir fichero
	ficheroDownloads.write("project_id, uri, type, filesize, information, downloadcount\n")
	for i in range(i, j) :
		repositorio = repositorios[i]
		downloads = repositorio.get_downloads() #Cogemos las "downloads" de cada repositorio
		try:
			count(downloads) #Comprobamos que tenga alguna
			sw = True
		except:
			sw = False	
		if sw == True :
			for download in downloads:	
			
				#Escribir al final del fichero
				try :
					ficheroDownloads.write('"' + repositorio.id + '", "')
				except :
					ficheroDownloads.write('"", "')
				try :
					ficheroDownloads.write(download.url + '", "')
				except :
					ficheroDownloads.write('", "')
				try :
					ficheroDownloads.write(download.content_type + '", "')
				except :
					ficheroDownloads.write('", "')
				try :
					ficheroDownloads.write(download.size + '", "')
				except :
					ficheroDownloads.write('", "')
				try :
					ficheroDownloads.write(download.description + '", "')
				except :
					ficheroDownloads.write('", "')
				try :
					ficheroDownloads.write(download.download_count + '"\n')
				except :
					ficheroDownloads.write('"\n')
					
		print "Loading: ", i
	ficheroDownloads.close() #Cerrar
else :
	print ("Este programa necesita dos parametros") 
	print ("Uso: $python proyectos.py n0 n1")

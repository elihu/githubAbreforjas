#Cojo los datos de downloads de cada proyecto
import github
import sys

def count(param):
   	acum = 0
	for a in param:
		acum = acum + 1
	return acum

if len(sys.argv) == 3: #Para poner un rango de usuarios que queremos ver
	i = int(sys.argv[1])
	j = int(sys.argv[2])
	
	datos = github.Github("user", "password")
	repositorios = datos.get_repos()
	for i in range(i, j) :
		repositorio = repositorios[i]
		print "--------------------"	
		print i
		print "name: ", repositorio.name
		downloads = repositorio.get_downloads() #Cogemos las "downloads" de cada repositorio
		try:
			print "downloads: ", count(downloads) #Comprobamos que tenga alguna
			sw = True
		except:
			print "No hay downloads"
			sw = False	
		print "--------------------"
		if sw == True :
			for download in downloads:		
				#project = models.ForeignKey('Projects', db_column='project')
				#uri = models.CharField(max_length=128L)
				print "Uri: ", download.url
				#type = models.CharField(max_length=128L, blank=True)
				print "Type: ", download.content_type
				#publication = models.DateTimeField(null=True, blank=True)
				#filesize = models.IntegerField(null=True, blank=True)
				print "Filesize: ", download.size
				#information = models.CharField(max_length=128L, null=True, blank=True)
				print "Information: ", download.description
				#downloadcount = models.IntegerField(null=True, db_column='downloadCount', blank=True) # Field name made lowercase.
				print "Downloadcount: ", download.download_count
				print "--------"
				print
		
		print "##############################################"
		print
else :
	print ("Este programa necesita dos parametros") 
	print ("Uso: $python proyectos.py n0 n1")

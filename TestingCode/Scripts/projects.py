import github
# -*- coding: iso-8859-15
import sys

#funcion para contar los elementos de un conjunto
def count(param):
   	acum = 0
	for a in param:
		acum = acum + 1
	return acum

#Se pasa como argumento de main el indice inicial y final de los proyectos que se quieren parsear		
if len(sys.argv) == 5:
        i = int(sys.argv[1])
	j = int(sys.argv[2])
	user = sys.argv[3]
	passwd = sys.argv[4]
	datos = github.Github(user, passwd) #Para evitar el limite de accesos que impone la api de github a usuarios anonimos hay que identificarse

	repositorios = datos.get_repos()
	for i in range(i, j):
		repo = repositorios[i]
		
		#Datos de models
		
		print "--------------------"	
		print i
		print "--------------------"
		
		print "external_id", repo.id
		print "name: ", repo.name
		#print "dataset"		
		print "homepage: ", repo.homepage		
		#print "sfpercentile"
		#print "sfdonation"
		#print "status"		
		print "created: ", repo.created_at		
		print "description: ", repo.description
		#print "sftotalnews"
		#print "sftotalposts"						
		try:
			print "totaltickets: ", count(repo.get_issues())
		except:
			print "Las issues no estan habilitadas"
		print "opentickets: ", repo.open_issues_count
		print "gcstars: ", count(repo.get_stargazers())
		try:
			print "gcactivities: ", count(repo.get_milestones())
		except:
			print "Las millestones no estan habilitadas"
		print "ghwatchers: ", repo.watchers_count
		print "repoforks: ", repo.forks_count
		if repo.private:		
			print "repoacces: private"
		else:
			print "repoacces: public"
		#print "repobrowse"	
		#print "totalreporeads"			
		print "totalrepowrites: ", count(repo.get_commits())
		#print "sfranking"
		#print "downloaddate"
		#print "processdate"						
		print "title: ", repo.full_name
		
		#Datos extra
		print "-----------------------------------"

		print "URL: ", repo.url
		print "Downloads: ", count(repo.get_downloads())
		try:
			print "Colaboradores: ", count(repo.get_collaborators())
		except:
			print "Los colaboradores no estan habilitados"
		print "Comments: ", count(repo.get_comments())
		print "Fecha actualizacion: ", repo.updated_at
		print "Tamaño: ", repo.size
		print "##############################################"
		print
else:
        print ("Este programa necesita un parámetro")
	print ("Uso: $python proyectos.py n0 n1")



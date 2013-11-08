import github
# -*- coding: iso-8859-15
import sys

def count(param):
   	acum = 0
	for a in param:
		acum = acum + 1
	return acum
		
if len(sys.argv) == 3:
        i = int(sys.argv[1])
        j = int(sys.argv[2])
	
	datos = github.Github("usuario", "contraseña")

	repositorios = datos.get_repos()
	for i in range(i, j):
		repo = repositorios[i]
		#print "Id " repo.id
		print "--------------------"	
		print i
		print "name: ", repo.name
		try:
			print "millestones: ", count(repo.get_milestones())
			sw = True
		except:
			print "Las millestones no estan habilitadas"
			sw = False	
		print "--------------------"
	
		if sw == True :
			milestones = repo.get_milestones()
			for mileston in milestones:
				print "externalID"			
				print "title", mileston.title
				print "due_on", mileston.due_on
				print "created", mileston.created_at
				print "state", mileston.state
				print "totaltickets", mileston.open_issues+mileston.closed_issues
	    			print "opentickets", mileston.open_issues
				print "completed_date"
				print "user", mileston.creator.login
				print "project",repo.name
				print "description", mileston.description
				print "descartado"
					
	'''try:
		print "totaltickets: ", count(repo.get_issues())
	except:
		print "Las issues no estan habilitadas"
	print "opentickets: ", repo.open_issues_count
	print "gcstars: ", count(repo.get_stargazers())
	
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
	print'''
else:
        print ("Este programa necesita un parámetro")
	print ("Uso: $python proyectos.py n0 n1")



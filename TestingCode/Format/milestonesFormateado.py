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
	print "title, due_on, created, state, totaltickets, opentickets, user, project, description"
	for i in range(i, j):
		repo = repositorios[i]		
		try:
			count(repo.get_milestones())
			sw = True
		except:
			sw = False	
		if sw == True :
			milestones = repo.get_milestones()
			for mileston in milestones:
				print mileston.title, " , ", mileston.due_on, " , ", mileston.created_at, " , ", mileston.state, " , ", mileston.open_issues+mileston.closed_issues, " , ", mileston.open_issues, " , ", mileston.creator.login, " , ", repo.name, " , ", mileston.description
					
else:
	print ("Este programa necesita un parámetro")
	print ("Uso: $python proyectos.py n0 n1")



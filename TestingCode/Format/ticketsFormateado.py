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
	
	print "project_id, project, ticket_id, created, updated, completed, title, description, totalcomments, status, author, owner, milestone"
	
	for i in range(i, j):
		repo = repositorios[i]
		
		try:
			count(repo.get_issues())
			sw = True
		except:
			sw = False	
	
		if sw == True :
			
			tickets = repo.get_issues()
			for ticket in tickets:
				print repo.id, " , ", repo.name, " , ", ticket.number, " , ", ticket.created_at, " , ", ticket.updated_at, " , ", ticket.state, " , ", ticket.title, " , ", '"'+ticket.body+'"', " , ", 
				try:
					print ticket.comments, " , ",
				except:
					print 0, " , ",
				print ticket.state, " , ", ticket.user.login, " , ",
				try:
					print ticket.assignee.login, " , ",
				except:
					print "no owner", " , ",
				try:
					print ticket.milestone.title
				except:
					print "no milestone"
				
									
else:
	print ("Este programa necesita un parámetro")
	print ("Uso: $python proyectos.py n0 n1")



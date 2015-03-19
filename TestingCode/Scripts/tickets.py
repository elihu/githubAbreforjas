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
			print "issues: ", count(repo.get_issues())
			sw = True
		except:
			print "Los issues no estan habilitadas"
			sw = False	
		print "--------------------"
	
		if sw == True :
			tickets = repo.get_issues()
			for ticket in tickets:
				
				print "project = ", repo.name
				print "externalID = ", ticket.number
				print "created = ", ticket.created_at
				print "updated = ", ticket.updated_at
				print "completed = ", ticket.state
				print "title = ", ticket.title
				print "description = ", ticket.body
				print "totalcomments = ", ticket.comments
				print "status = ", ticket.state
				print "priority = #"
				print "type = #" 
				print "author = ", ticket.user.login
				try:
					print "owner = ", ticket.assignee.login
				except:
					print "No owner"
				try:
					print "milestone = ", ticket.milestone.title
				except:
					print "No milestone"
				print "votes = #"
				#####
				'''print "title", mileston.title
				print "due_on", mileston.due_on
				print "created", mileston.created_at
				print "state", mileston.state
				print "totaltickets", mileston.open_issues+mileston.closed_issues
	    			print "opentickets", mileston.open_issues
				print "completed_date"
				print "user", mileston.creator.login
				print "project",repo.name
				print "description", mileston.description
				print "descartado" '''
					
else:
        print ("Este programa necesita un parámetro")
	print ("Uso: $python proyectos.py n0 n1")



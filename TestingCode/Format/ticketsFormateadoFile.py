import github
# -*- coding: iso-8859-15
import sys
import codecs

def count(param):
   	acum = 0
	for a in param:
		acum = acum + 1
	return acum
		
if len(sys.argv) == 3:
        i = int(sys.argv[1])
        j = int(sys.argv[2])
	
	datos = github.Github("u", "c")
	repositorios = datos.get_repos()
	
	fichero = codecs.open("tickets.csv", "a", "utf-8") #Abrir fichero
	
	fichero.write("project_id, project, ticket_id, created, updated, completed, title, totalcomments, status, author, owner, milestone\n")
	#fichero.write('\n')
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
				try:
					fichero.write('"'+str(repo.id)+'", "')
				except:
					fichero.write('"", "')
				try:
					fichero.write (repo.name+'", "')
				except:
					fichero.write('", "')
				try:
					fichero.write(str(ticket.number) +'", "')
				except:
					fichero.write('", "')
				try:
					fichero.write(str(ticket.created_at) +'", "')
				except:
					fichero.write('", "')
				try:
					fichero.write( str(ticket.updated_at) +'", "')
				except:
					fichero.write('", "')
				try:
					fichero.write( ticket.state +'", "')
				except:
					fichero.write('", "')
				try:
					fichero.write( str(ticket.title) +'", "')
				except:
					fichero.write('", "')
				''' - He quitado la descripcion ya que no tiene utilidad para metricas y provocaba errores por su longitud y los saltos de linea
				try:
					fichero.write( str(ticket.body) +'", "')
				except:
					fichero.write('", "')'''
				try:
					fichero.write( str(ticket.comments) +'", "')
				except:
					fichero.write('0", "')
				try:
					fichero.write(ticket.state  +'", "')
				except:
					fichero.write('", "')
				try:
					fichero.write(ticket.user.login  +'", "')
				except:
					fichero.write('", "')
				try:
					fichero.write( ticket.assignee.login +'", "')
				except:
					fichero.write('no owner", "')
				try:
					fichero.write( ticket.milestone.title +'"\n')
				except:
					fichero.write('no milestone"\n')
				
			print i	
	fichero.close()					
else:
	print ("Este programa necesita un parámetro")
	print ("Uso: $python script.py n0 n1")



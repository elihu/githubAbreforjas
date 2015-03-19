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
	
	fichero = codecs.open("milestones.csv", "a", "utf-8") #Abrir fichero
	
	#fichero.write("title, due_on, created, state, totaltickets, opentickets, user, project, description\n")
	
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
				try:
					fichero.write ('"'+mileston.title+'", "')
				except:
					fichero.write('"", "')
				try:
					fichero.write( mileston.due_on +'", "')
				except:
					fichero.write('", "')
				try:
					fichero.write(str(mileston.created_at)+'", "')
				except:
					fichero.write('", "')
				try:
					fichero.write(mileston.state +'", "')
				except:
					fichero.write('", "')
				try:
					fichero.write(str(mileston.open_issues+mileston.closed_issues) +'", "')
				except:
					fichero.write('0", "')
				try:
					fichero.write(str(mileston.open_issues) +'", "')
				except:
					fichero.write('0", "')
				try:
					fichero.write(mileston.creator.login +'", "')
				except:
					fichero.write('", "')
				try:
					fichero.write(repo.name +'", "')
				except:
					fichero.write('", "')
				try:
					fichero.write(str(mileston.description)+'"\n')
				except:
					fichero.write('" \n')
					
		print i
	fichero.close()
else:
	print ("Este programa necesita un parámetro")
	print ("Uso: $python proyectos.py n0 n1")



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
	datos = github.Github("usuario", "contraseña")

	repositorios = datos.get_repos()
	fichero = codecs.open("projects.csv", "a", "utf-8") #Abrir fichero
	#fichero.write("external_id, name, homepage, created, description, totaltickets, opentickets, gcstars, gcactivities, ghwatchers, repoforks, repoacces, totalrepowrites, title, url, downloads, colaborators, comments, update_date, size, language")
	#fichero.write('"\n')
	for i in range(i, j):
		repo = repositorios[i]
		try :
			fichero.write('"' + str(repo.id) + '", "')
		except :
			fichero.write('", "')
		try :
			fichero.write(repo.name + '", "')
		except :
			fichero.write('", "')
		try :
			fichero.write(repo.homepage + '", "')
		except :
			fichero.write('", "')
		try :
			fichero.write(str(repo.created_at) + '", "')
		except :
			fichero.write('", "')
		try :
			fichero.write(repo.description + '", "')
		except :
			fichero.write('", "')
		
		try:
			fichero.write(str(count(repo.get_issues()))+ '", "')
		except:
			fichero.write(str(0) +'", "')
		try :
			fichero.write(str(repo.open_issues_count) + '", "')
		except :
			fichero.write(str(0) +'", "')
		
		try :
			fichero.write(str(count(repo.get_stargazers())) + '", "')
		except :
			fichero.write(str(0) +'", "')
		try :		
			fichero.write(str(count(repo.get_milestones())) + '", "')
		except :
			fichero.write(str(0) +'", "')
		try :
			fichero.write(str(repo.watchers_count) + '", "')
		except :
			fichero.write(str(0) +'", "')
		try :
			fichero.write(str(repo.forks_count) + '", "')
		except :
			fichero.write(str(0) +'", "')
		if repo.private:
			try :
				fichero.write('private" ,"')
			except :
				fichero.write('", "')
		else:
			try :
				fichero.write('public", "')
			except :
				fichero.write('", "')
		try :
			fichero.write(str(count(repo.get_commits())) + '", "')
		except :
			fichero.write('", "')
		try :
			fichero.write(repo.full_name + '", "')
		except :
			fichero.write('", "')
		try :
			fichero.write(repo.url + '", "')
		except :
			fichero.write('", "')
		try :
			fichero.write(str(count(repo.get_downloads())) + '", "')
		except :
			fichero.write('0", "')
		try :
			fichero.write(str(count(repo.get_collaborators())) + '", "')
		except :
			fichero.write('0", "')
		try :
			fichero.write(str(count(repo.get_comments())) + '", "')
		except :
			fichero.write('0", "')
		try :
			fichero.write(str(repo.updated_at) + '", "')
		except :
			fichero.write('", "')
		try :
			fichero.write(str(repo.size) + '", "')
		except :
			fichero.write('", "')
		try :
			fichero.write(repo.language + '"')
		except :
			fichero.write('"')
		fichero.write('\n')
		print i
	fichero.close()
		
else:
	print ("Este programa necesita un parámetro")
	print ("Uso: $python proyectos.py n0 n1")



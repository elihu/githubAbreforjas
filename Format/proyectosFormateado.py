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
	
	print "external_id, name, homepage, created, description, totaltickets, opentickets, gcstars, gcactivities, ghwatchers, repoforks, repoacces, totalrepowrites, title, url, downloads, colaborators, comments, update_date, size, language"
	for i in range(i, j):
		repo = repositorios[i]
		
		
		print repo.id, " , ", repo.name, " , ", repo.homepage, " , ", repo.created_at, " , ", repo.description, " , ",
		try:
			print count(repo.get_issues()), " , ",
		except:
			print 0, " , ",
		print repo.open_issues_count, " , ",count(repo.get_stargazers()), " , ",
		try:
			print count(repo.get_milestones()), " , ",
		except:
			print 0, " , ",
		print repo.watchers_count, " , ",repo.forks_count, " , ",
		if repo.private:		
			print "private", " , ",
		else:
			print "public", " , ",
			
		print count(repo.get_commits()), " , ", repo.full_name, " , ", repo.url, " , ", count(repo.get_downloads()), " , ",
		try:
			print count(repo.get_collaborators()), " , ",
		except:
			print 0, " , ",
		print count(repo.get_comments()), " , ", repo.updated_at, " , ", repo.size, " , ", repo.language
		
else:
	print ("Este programa necesita un parámetro")
	print ("Uso: $python proyectos.py n0 n1")



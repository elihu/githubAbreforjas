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
	slices = codecs.open("projects_slice.csv", "w", "utf-8") #Abrir slices
	table = codecs.open("projects_table.csv", "w", "utf-8") #Abrir table
	
	'''fichero.write("project, name, homepage, year, description, totaltickets, opentickets, gcstars, gcactivities, ghwatchers, repoforks, repoacces, totalrepowrites, title, url, downloads, colaborators, comments, update_date, size, language")'''
	
	
	table.write("project, name, description\n");
	slices.write("project, year, totaltickets, opentickets, gcstars, totalrepowrites\n")
	
	for i in range(i, j):
		repo = repositorios[i]
		try :
			slices.write('"' + str(repo.id) + '"')
			table.write('"' + str(repo.id) + '"')
		except :
			slices.write('""')
			table.write('""')
		try :
			table.write(', "'+repo.name + '"')
		except :
			table.write('""')
		'''try :
			slices.write(repo.homepage + '", "')
		except :
			slices.write('", "')
		'''	
		try :
			slices.write(', "'+ str(repo.created_at)[0:4] + '"')
		except :
			slices.write('""')
		try :
			table.write(', "' + repo.description + '"')
		except :
			table.write('""')
		
		try:
			slices.write(', "' + str(count(repo.get_issues()))+ '"')
		except:
			slices.write(', "' + str(0) +'"')
		try :
			slices.write(', "' + str(repo.open_issues_count) + '"')
		except :
			slices.write(', "' + str(0) +'"')
		
		try :
			slices.write(', "' + str(count(repo.get_stargazers())) + '"')
		except :
			slices.write(', "' + str(0) +'"')
		'''
		try :		
			slices.write(str(count(repo.get_milestones())) + '", "')
		except :
			slices.write(str(0) +'", "')
		try :
			slices.write(str(repo.watchers_count) + '", "')
		except :
			slices.write(str(0) +'", "')
		try :
			slices.write(str(repo.forks_count) + '", "')
		except :
			slices.write(str(0) +'", "')
		if repo.private:
			try :
				slices.write('private" ,"')
			except :
				slices.write('", "')
		else:
			try :
				slices.write('public", "')
			except :
				slices.write('", "')
		'''
		try :
			slices.write(', "' + str(count(repo.get_commits())) + '"')
		except :
			slices.write('""')
		'''
		try :
			slices.write(repo.full_name + '", "')
		except :
			slices.write('", "')
		try :
			slices.write(repo.url + '", "')
		except :
			slices.write('", "')
		try :
			slices.write(str(count(repo.get_downloads())) + '", "')
		except :
			slices.write('0", "')
		try :
			slices.write(str(count(repo.get_collaborators())) + '", "')
		except :
			slices.write('0", "')
		try :
			slices.write(str(count(repo.get_comments())) + '", "')
		except :
			slices.write('0", "')
		try :
			slices.write(str(repo.updated_at) + '", "')
		except :
			slices.write('", "')
		try :
			slices.write(str(repo.size) + '", "')
		except :
			slices.write('", "')
		try :
			slices.write(repo.language + '"')
		except :
			slices.write('"')'''
		slices.write('\n')
		table.write('\n')
		print i
	slices.close()
	table.close()
		
else:
	print ("Este programa necesita un parámetro")
	print ("Uso: $python proyectos.py n0 n1")



import github
datos = github.Github()

repositorios = datos.get_repos()
for repo in repositorios:
        #print "Id " repo.id
        print "Nombre " + repo.name
        print "Descripcion " + repo.description
        print "URL " + repo.url
        print
        print "##############################################"
        print

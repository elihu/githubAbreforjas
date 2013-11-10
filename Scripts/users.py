import github
import sys

if len(sys.argv) == 3: #Para poner un rango de usuarios que queremos ver
	i = int(sys.argv[1])
	j = int(sys.argv[2])
	
	datos = github.Github("user", "password")
	usuarios = datos.get_users()
	for i in range(i, j) :
		usuario = usuarios[i]
		
		print "--------------------"	
		print i
		print "--------------------"
		
		#external_id = models.CharField(max_length=128L)
		print "Id: ", usuario.id
		#forge = models.CharField(max_length=128L, blank=True) Estaba comentado desde el archivo models
		#dataset = models.ForeignKey(Datasets)
		#username = models.CharField(max_length=128L, blank=True)
		print "username: ", usuario.login
		#name = models.CharField(max_length=128L, blank=True)
		print "name: ", usuario.name
		#email = models.CharField(max_length=128L, blank=True, null=True)
		print "email: ", usuario.email
		#created = models.DateTimeField(null=True, blank=True)
		print "created: ", usuario.created_at
		
		
		print "##############################################"
		print
else :
	print ("Este programa necesita dos parametros") 
	print ("Uso: $python proyectos.py n0 n1")

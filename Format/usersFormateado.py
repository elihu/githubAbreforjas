import github
import sys
import codecs

if len(sys.argv) == 3: #Para poner un rango de usuarios que queremos ver
	i = int(sys.argv[1])
	j = int(sys.argv[2])
	
	datos = github.Github("user", "password")
	usuarios = datos.get_users()
	ficheroUsers = codecs.open("users.csv", "w", "utf-8") #Abrir fichero
	ficheroUsers.write("id, username, name, email, created\n")
	for i in range(i, j) :
		usuario = usuarios[i]
		
		#Escribir al final del fichero
		try :
			ficheroUsers.write('"' + str(usuario.id) + '", "')
		except :
			ficheroUsers.write('"", "')
		try :
			ficheroUsers.write(usuario.login + '", "')
		except :
			ficheroUsers.write('", "')
		try :
			ficheroUsers.write(usuario.name + '", "')
		except :
			ficheroUsers.write('", "')
		try :
			ficheroUsers.write(usuario.email + '", "')
		except :
			ficheroUsers.write('", "')
		try :
			ficheroUsers.write(str(usuario.created_at) + '"\n')
		except :
			ficheroUsers.write('"\n')
		
		print "Loading: ", i
	ficheroUsers.close() #Cerrar
else :
	print ("Este programa necesita dos parametros") 
	print ("Uso: $python proyectos.py n0 n1")

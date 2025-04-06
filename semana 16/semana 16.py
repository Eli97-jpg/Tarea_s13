#Creamos el archivo

escribir = open("my_notes.txt","w")  #Creamos la carpeta y colocamos write

try:
    #Con ayuda del metodo write escribirmos texto
    escribir.write("Hola mundo\n")
    escribir.write("Estoy escribiendo archivos en python\n")
    escribir.write("Aprenderemos a escribir y visualizar")

finally:
    escribir.close()  #Cerramos el archivo
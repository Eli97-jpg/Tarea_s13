#Visualizar texto

escribir = open("my_notes.txt","r") #Abrimos el archivo txt y colocamos r de read

visualizar = escribir.readline()  #Creamos el metodo readline que nos indica la primera linea
print(visualizar)  #Imprimimos la primera linea

#Creamos un bocle for que recorrera las demas lineas
try:
    for i in escribir:

        print(i)  #Imprimimos

finally:
    escribir.close() #Cerramos el archivo